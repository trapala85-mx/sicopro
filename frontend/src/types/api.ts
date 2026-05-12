export interface ApiResponse<T> {
  success: boolean;
  status_code: number;
  msg: string;
  data: T; // ¡Aquí está la magia! T puede ser cualquier cosa
}
