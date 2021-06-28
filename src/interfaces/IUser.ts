export interface ITokens {
  refresh: string;
  access: string;
}

export interface IUser {
  tokens: ITokens;
  name: string;
  msg: string;
  email: string;
}
