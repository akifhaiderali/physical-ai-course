/**
 * useTextSelection Hook
 *
 * Custom React hook for capturing user text selection from the page
 */

import { useState, useEffect } from 'react';
import { useLocation } from '@docusaurus/router';

/**
 * Hook to capture selected text from the page
 *
 * @returns Currently selected text (empty string if no selection)
 */
export function useTextSelection(): string {
  const [selectedText, setSelectedText] = useState<string>('');
  const location = useLocation();

  useEffect(() => {
    // Only run on client-side (browser), not during SSR
    if (typeof window === 'undefined') return;

    const handleSelection = () => {
      const selection = window.getSelection();
      const text = selection?.toString().trim() || '';
      setSelectedText(text);
    };

    // Listen for mouseup events (when user releases mouse after selecting)
    document.addEventListener('mouseup', handleSelection);

    // Listen for touchend events (for mobile devices)
    document.addEventListener('touchend', handleSelection);

    return () => {
      document.removeEventListener('mouseup', handleSelection);
      document.removeEventListener('touchend', handleSelection);
    };
  }, []);

  // Clear selection when route changes (user navigates to different page)
  useEffect(() => {
    // Only run on client-side
    if (typeof window === 'undefined') return;

    setSelectedText('');

    // Also clear browser selection
    const selection = window.getSelection();
    if (selection) {
      selection.removeAllRanges();
    }
  }, [location.pathname]);

  return selectedText;
}
