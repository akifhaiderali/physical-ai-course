/**
 * ChatMessage Component
 *
 * Displays individual chat messages with source references
 */

import React from 'react';
import { ChatMessageData } from './ChatbotWidget';
import styles from './styles.module.css';

interface ChatMessageProps {
  message: ChatMessageData;
}

const ChatMessage: React.FC<ChatMessageProps> = ({ message }) => {
  const { role, content, sources, timestamp } = message;

  const formatTime = (date: Date) => {
    return date.toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit' });
  };

  return (
    <div className={`${styles.message} ${styles[`message-${role}`]}`}>
      <div className={styles.messageHeader}>
        <span className={styles.messageRole}>
          {role === 'user' ? 'You' : role === 'assistant' ? 'Assistant' : 'System'}
        </span>
        <span className={styles.messageTime}>{formatTime(timestamp)}</span>
      </div>

      <div className={styles.messageContent}>
        {content.split('\n').map((line, idx) => (
          <p key={idx}>{line}</p>
        ))}
      </div>

      {sources && sources.length > 0 && (
        <div className={styles.sources}>
          <details>
            <summary className={styles.sourcesToggle}>
              Sources ({sources.length})
            </summary>
            <div className={styles.sourcesList}>
              {sources.map((source, idx) => (
                <div key={idx} className={styles.source}>
                  <div className={styles.sourceHeader}>
                    <strong>
                      {source.chapter}
                      {source.section && ` - ${source.section}`}
                    </strong>
                    <span className={styles.relevanceScore}>
                      {(source.relevance_score * 100).toFixed(0)}% match
                    </span>
                  </div>
                  <p className={styles.sourceText}>{source.text}</p>
                  {source.metadata && Object.keys(source.metadata).length > 0 && (
                    <div className={styles.sourceMetadata}>
                      {Object.entries(source.metadata).map(([key, value]) => (
                        <span key={key} className={styles.metadataItem}>
                          {key}: {value}
                        </span>
                      ))}
                    </div>
                  )}
                </div>
              ))}
            </div>
          </details>
        </div>
      )}
    </div>
  );
};

export default ChatMessage;
