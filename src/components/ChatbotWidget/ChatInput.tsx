/**
 * ChatInput Component
 *
 * Text input field with submit button for chatbot queries
 */

import React, { useState, KeyboardEvent } from 'react';
import styles from './styles.module.css';

interface ChatInputProps {
  onSubmit: (query: string) => void;
  disabled?: boolean;
  mode: 'full-book' | 'selected-text';
  hasSelectedText: boolean;
}

const ChatInput: React.FC<ChatInputProps> = ({ onSubmit, disabled = false, mode, hasSelectedText }) => {
  const [input, setInput] = useState('');

  const handleSubmit = () => {
    if (!input.trim() || disabled) return;
    onSubmit(input);
    setInput('');
  };

  const handleKeyPress = (e: KeyboardEvent<HTMLTextAreaElement>) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSubmit();
    }
  };

  const getPlaceholder = () => {
    if (mode === 'selected-text' && !hasSelectedText) {
      return 'Please select text on the page first...';
    }
    return mode === 'full-book' ? 'Ask a question about the book...' : 'Ask about the selected text...';
  };

  return (
    <div className={styles.inputContainer}>
      <textarea
        className={styles.input}
        value={input}
        onChange={(e) => setInput(e.target.value)}
        onKeyPress={handleKeyPress}
        placeholder={getPlaceholder()}
        disabled={disabled}
        rows={2}
        maxLength={1000}
      />
      <button
        className={styles.submitButton}
        onClick={handleSubmit}
        disabled={disabled || !input.trim()}
        aria-label="Send message"
      >
        {disabled ? '...' : 'Send'}
      </button>
    </div>
  );
};

export default ChatInput;
