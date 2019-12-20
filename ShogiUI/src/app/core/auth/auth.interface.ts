export interface LoginResponse {
    content: {
        status: boolean;
        userId: number;
    }
}

export interface RegisterResponse {
    content: {
        status: boolean;
        errorMsg: string;
    }
}
