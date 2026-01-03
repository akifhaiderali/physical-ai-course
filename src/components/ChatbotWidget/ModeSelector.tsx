/**
 * ModeSelector Component
 *
 * Toggle between full-book and selected-text RAG modes
 */

import React from 'react';
import styles from './styles.module.css';

interface ModeSelectorProps {
  mode: 'full-book' | 'selected-text';
  onModeChange: (mode: 'full-book' | 'selected-text') => void;
  selectedText: string;
}

const ModeSelector: React.FC<ModeSelectorProps> = ({ mode, onModeChange, selectedText }) => {
  return (
    <div className={styles.modeSelector}>
      <button
        className={`${styles.modeButton} ${mode === 'full-book' ? styles.modeButtonActive : ''}`}
        onClick={() => onModeChange('full-book')}
        aria-pressed={mode === 'full-book'}
      >
        <span className={styles.modeIcon}>📚</span>
        <span className={styles.modeLabel}>Ask about the book</span>
      </button>

      <button
        className={`${styles.modeButton} ${mode === 'selected-text' ? styles.modeButtonActive : ''}`}
        onClick={() => onModeChange('selected-text')}
        aria-pressed={mode === 'selected-text'}
        disabled={!selectedText}
        title={!selectedText ? 'Please select text on the page first' : 'Ask about selected text'}
      >
        <span className={styles.modeIcon}>✨</span>
        <span className={styles.modeLabel}>
          Explain selected text
          {selectedText && <span className={styles.selectionIndicator}> ({selectedText.length} chars)</span>}
        </span>
      </button>
    </div>
  );
};

export default ModeSelector;
