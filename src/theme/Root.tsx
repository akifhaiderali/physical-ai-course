/**
 * Docusaurus Root Component Wrapper
 *
 * Swizzled Root component that includes the ChatbotWidget on all pages
 */

import React from 'react';
import BrowserOnly from '@docusaurus/BrowserOnly';

// Functional chatbot component with backend integration
function SimpleChatbot() {
  const [isOpen, setIsOpen] = React.useState(false);
  const [messages, setMessages] = React.useState([]);
  const [input, setInput] = React.useState('');
  const [isLoading, setIsLoading] = React.useState(false);

  const sendQuery = async () => {
    if (!input.trim() || isLoading) return;

    const userMsg = { role: 'user', content: input, id: Date.now() };
    setMessages(prev => [...prev, userMsg]);
    setInput('');
    setIsLoading(true);

    try {
      const response = await fetch('http://localhost:8000/api/v1/chat/query', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ query: input, mode: 'full-book' }),
      });
      const data = await response.json();

      setMessages(prev => [...prev, {
        role: 'assistant',
        content: data.answer_text,
        sources: data.sources,
        id: Date.now() + 1
      }]);
    } catch (error) {
      setMessages(prev => [...prev, {
        role: 'system',
        content: 'Error: Could not connect to backend. Make sure http://localhost:8000 is running.',
        id: Date.now() + 1
      }]);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div style={{ position: 'fixed', bottom: '24px', right: '24px', zIndex: 9999 }}>
      {!isOpen && (
        <button
          onClick={() => setIsOpen(true)}
          style={{
            width: '60px',
            height: '60px',
            borderRadius: '50%',
            background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
            border: 'none',
            cursor: 'pointer',
            fontSize: '28px',
            boxShadow: '0 4px 12px rgba(0, 0, 0, 0.15)',
          }}
        >
          💬
        </button>
      )}
      {isOpen && (
        <div style={{
          width: '400px',
          height: '600px',
          background: 'white',
          borderRadius: '12px',
          boxShadow: '0 8px 32px rgba(0, 0, 0, 0.12)',
          display: 'flex',
          flexDirection: 'column',
        }}>
          {/* Header */}
          <div style={{
            background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
            color: 'white',
            padding: '16px',
            borderRadius: '12px 12px 0 0',
            display: 'flex',
            justifyContent: 'space-between',
            alignItems: 'center'
          }}>
            <h3 style={{ margin: 0, fontSize: '18px' }}>Course Assistant</h3>
            <button onClick={() => setIsOpen(false)} style={{ background: 'none', border: 'none', color: 'white', cursor: 'pointer', fontSize: '24px' }}>✕</button>
          </div>

          {/* Messages */}
          <div style={{ flex: 1, overflowY: 'auto', padding: '16px', background: '#fafafa' }}>
            {messages.length === 0 && (
              <p style={{ color: '#666', fontSize: '14px' }}>👋 Ask me anything about the course!</p>
            )}
            {messages.map((msg) => (
              <div key={msg.id} style={{
                marginBottom: '12px',
                padding: '12px',
                borderRadius: '8px',
                background: msg.role === 'user' ? 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)' : 'white',
                color: msg.role === 'user' ? 'white' : '#333',
                maxWidth: '85%',
                marginLeft: msg.role === 'user' ? 'auto' : '0',
                marginRight: msg.role === 'user' ? '0' : 'auto',
                fontSize: '14px',
                lineHeight: '1.5',
                border: msg.role !== 'user' ? '1px solid #e0e0e0' : 'none'
              }}>
                <div style={{ whiteSpace: 'pre-wrap' }}>{msg.content}</div>
                {msg.sources && msg.sources.length > 0 && (
                  <details style={{ marginTop: '8px', fontSize: '12px' }}>
                    <summary style={{ cursor: 'pointer', fontWeight: 'bold' }}>Sources ({msg.sources.length})</summary>
                    {msg.sources.map((src, i) => (
                      <div key={i} style={{ marginTop: '4px', padding: '8px', background: 'rgba(0,0,0,0.05)', borderRadius: '4px' }}>
                        <strong>{src.chapter}</strong> ({(src.relevance_score * 100).toFixed(0)}% match)
                      </div>
                    ))}
                  </details>
                )}
              </div>
            ))}
            {isLoading && <div style={{ color: '#666', fontSize: '14px' }}>💭 Thinking...</div>}
          </div>

          {/* Input */}
          <div style={{ padding: '12px', background: 'white', borderTop: '1px solid #e0e0e0', display: 'flex', gap: '8px' }}>
            <input
              type="text"
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyPress={(e) => e.key === 'Enter' && sendQuery()}
              placeholder="Ask a question..."
              disabled={isLoading}
              style={{
                flex: 1,
                padding: '10px',
                border: '2px solid #e0e0e0',
                borderRadius: '8px',
                fontSize: '14px',
                outline: 'none',
              }}
            />
            <button
              onClick={sendQuery}
              disabled={isLoading || !input.trim()}
              style={{
                padding: '10px 20px',
                background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
                color: 'white',
                border: 'none',
                borderRadius: '8px',
                cursor: isLoading || !input.trim() ? 'not-allowed' : 'pointer',
                fontSize: '14px',
                fontWeight: 'bold',
                opacity: isLoading || !input.trim() ? 0.5 : 1,
              }}
            >
              Send
            </button>
          </div>
        </div>
      )}
    </div>
  );
}

export default function Root({ children }: { children: React.ReactNode }) {
  return (
    <>
      {children}
      <BrowserOnly fallback={<div />}>
        {() => <SimpleChatbot />}
      </BrowserOnly>
    </>
  );
}
