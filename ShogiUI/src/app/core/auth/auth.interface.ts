export interface LoginResponse {
    content: {
        status: boolean;
        user_id: number;
    }
}

export interface RegisterResponse {
    content: {
        status: boolean;
        errorMsg: string;
    }
}
