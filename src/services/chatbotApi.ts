/**
 * Chatbot API Client
 *
 * Frontend service for communicating with the RAG Chatbot backend
 */

import axios, { AxiosInstance } from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_BASE_URL || 'http://localhost:8000/api/v1';

/**
 * Query request payload
 */
export interface QueryRequest {
  query: string;
  mode: 'full-book' | 'selected-text';
  selected_text?: string;
  session_id?: string;
}

/**
 * Retrieved passage from vector database
 */
export interface RetrievedPassage {
  text: string;
  chapter: string;
  section: string;
  relevance_score: number;
  metadata?: Record<string, any>;
}

/**
 * Query processing metadata
 */
export interface QueryMetadata {
  query_id: string;
  timestamp: string;
  processing_time_ms: number;
  tokens_used: number;
  mode: 'full-book' | 'selected-text';
}

/**
 * Answer response from backend
 */
export interface Answer {
  answer_text: string;
  sources: RetrievedPassage[];
  mode: 'full-book' | 'selected-text';
  query_metadata: QueryMetadata;
  warning?: string;
}

/**
 * Health status response
 */
export interface HealthStatus {
  status: 'healthy' | 'unhealthy';
  timestamp: string;
  dependencies: {
    vector_db: 'healthy' | 'unhealthy';
    llm_api: 'healthy' | 'unhealthy';
  };
}

/**
 * Error response
 */
export interface ErrorResponse {
  error: string;
  message: string;
  status_code: number;
}

/**
 * Chatbot API Client
 */
class ChatbotApiClient {
  private client: AxiosInstance;

  constructor() {
    this.client = axios.create({
      baseURL: API_BASE_URL,
      headers: {
        'Content-Type': 'application/json',
      },
      timeout: 30000, // 30 second timeout
    });
  }

  /**
   * Submit a chatbot query
   *
   * @param request - Query request payload
   * @returns Answer response
   */
  async submitQuery(request: QueryRequest): Promise<Answer> {
    try {
      const response = await this.client.post<Answer>('/chat/query', request);
      return response.data;
    } catch (error) {
      if (axios.isAxiosError(error) && error.response) {
        const errorData = error.response.data as ErrorResponse;
        throw new Error(errorData.message || 'Failed to submit query');
      }
      throw new Error('Network error: Unable to reach chatbot API');
    }
  }

  /**
   * Check health status of backend
   *
   * @returns Health status
   */
  async healthCheck(): Promise<HealthStatus> {
    try {
      const response = await this.client.get<HealthStatus>('/health');
      return response.data;
    } catch (error) {
      throw new Error('Health check failed');
    }
  }
}

// Export singleton instance
export const chatbotApi = new ChatbotApiClient();

// Export individual functions for convenience
export const submitQuery = (request: QueryRequest) => chatbotApi.submitQuery(request);
export const healthCheck = () => chatbotApi.healthCheck();
