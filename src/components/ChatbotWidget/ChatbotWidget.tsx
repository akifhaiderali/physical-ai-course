/**
 * ChatbotWidget Component
 *
 * Main chatbot component with floating icon and panel
 */

import React, { useState } from 'react';
import { submitQuery, Answer, QueryRequest } from '../../services/chatbotApi';
import { useTextSelection } from '../TextSelectionCapture/useTextSelection';
import ChatInput from './ChatInput';
import ChatMessage from './ChatMessage';
import ModeSelector from './ModeSelector';
import styles from './styles.module.css';

export interface ChatMessageData {
  id: string;
  role: 'user' | 'assistant' | 'system';
  content: string;
  timestamp: Date;
  sources?: Answer['sources'];
}

const ChatbotWidget: React.FC = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [mode, setMode] = useState<'full-book' | 'selected-text'>('full-book');
  const [messages, setMessages] = useState<ChatMessageData[]>([]);
  const [isLoading, setIsLoading] = useState(false);

  const selectedText = useTextSelection();

  const handleToggle = () => {
    setIsOpen(!isOpen);
    if (!isOpen) {
      // Show welcome message when opening
      if (messages.length === 0) {
        setMessages([
          {
            id: '0',
            role: 'system',
            content:
              'Welcome! I can help answer questions about the Physical AI & Humanoid Robotics course. Choose a mode:\n\n' +
              '• **Ask about the book**: Search the entire book for answers\n' +
              '• **Explain selected text**: Get clarification on highlighted text',
            timestamp: new Date(),
          },
        ]);
      }
    }
  };

  const handleSubmit = async (query: string) => {
    if (!query.trim()) return;

    // Add user message
    const userMessage: ChatMessageData = {
      id: Date.now().toString(),
      role: 'user',
      content: query,
      timestamp: new Date(),
    };
    setMessages((prev) => [...prev, userMessage]);

    // Prepare request
    const request: QueryRequest = {
      query,
      mode,
      ...(mode === 'selected-text' && { selected_text: selectedText }),
    };

    setIsLoading(true);

    try {
      const answer = await submitQuery(request);

      // Add assistant message
      const assistantMessage: ChatMessageData = {
        id: answer.query_metadata.query_id,
        role: 'assistant',
        content: answer.answer_text,
        timestamp: new Date(answer.query_metadata.timestamp),
        sources: answer.sources,
      };
      setMessages((prev) => [...prev, assistantMessage]);

      // Show warning if present
      if (answer.warning) {
        const warningMessage: ChatMessageData = {
          id: `${answer.query_metadata.query_id}-warning`,
          role: 'system',
          content: `⚠️ ${answer.warning}`,
          timestamp: new Date(),
        };
        setMessages((prev) => [...prev, warningMessage]);
      }
    } catch (error) {
      const errorMessage: ChatMessageData = {
        id: `error-${Date.now()}`,
        role: 'system',
        content: `Error: ${error instanceof Error ? error.message : 'Failed to get response'}`,
        timestamp: new Date(),
      };
      setMessages((prev) => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  const handleModeChange = (newMode: 'full-book' | 'selected-text') => {
    setMode(newMode);

    // Show guidance for selected-text mode if no text is selected
    if (newMode === 'selected-text' && !selectedText) {
      const guidanceMessage: ChatMessageData = {
        id: `guidance-${Date.now()}`,
        role: 'system',
        content: 'Please highlight some text on the page first, then ask your question.',
        timestamp: new Date(),
      };
      setMessages((prev) => [...prev, guidanceMessage]);
    }
  };

  return (
    <div className={styles.chatbotWidget}>
      {/* Floating button */}
      {!isOpen && (
        <button className={styles.floatingButton} onClick={handleToggle} aria-label="Open chatbot">
          <span className={styles.icon}>💬</span>
        </button>
      )}

      {/* Chat panel */}
      {isOpen && (
        <div className={styles.chatPanel}>
          {/* Header */}
          <div className={styles.header}>
            <h3>Course Assistant</h3>
            <button className={styles.closeButton} onClick={handleToggle} aria-label="Close chatbot">
              ✕
            </button>
          </div>

          {/* Mode selector */}
          <ModeSelector mode={mode} onModeChange={handleModeChange} selectedText={selectedText} />

          {/* Messages */}
          <div className={styles.messages}>
            {messages.map((msg) => (
              <ChatMessage key={msg.id} message={msg} />
            ))}
            {isLoading && (
              <div className={styles.loadingIndicator}>
                <span>Thinking...</span>
              </div>
            )}
          </div>

          {/* Input */}
          <ChatInput
            onSubmit={handleSubmit}
            disabled={isLoading || (mode === 'selected-text' && !selectedText)}
            mode={mode}
            hasSelectedText={!!selectedText}
          />
        </div>
      )}
    </div>
  );
};

export default ChatbotWidget;
