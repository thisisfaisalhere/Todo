import axiosInstance from "axios";
import { IUser } from "../interfaces/IUser";

const url = process.env.REACT_APP_BACKEND_URL;

let user: IUser;

// TODO: get current user

const axios = axiosInstance.create({
  baseURL: url,
  timeout: 5000,
  headers: {
    // Authorization: user ? `JWT ${user?.tokens.access}` : null,
    accept: "application/json",
  },
});

axios.interceptors.response.use(
  (response) => {
    return response;
  },
  async function (error) {
    const originalRequest = error.config;
    if (typeof error.response === "undefined") {
      alert(
        `A server/network error occurred.\n
        Looks like CORS might be the problem.\n
        Sorry about this - we will get it fixed shortly.`
      );
      return Promise.reject(error);
    }

    if (
      error.response.status === 401 &&
      error.response.statusText === "Unauthorized"
    ) {
      const refreshToken = user.tokens.refresh;
      if (refreshToken) {
        const tokenParts = JSON.parse(atob(refreshToken.split(".")[1]));

        const now = Math.ceil(Date.now() / 1000);
        console.log(tokenParts.exp);

        if (tokenParts.exp > now) {
          return axios
            .post("api/user/token/refresh/", { refresh: refreshToken })
            .then((response) => {
              user.tokens.access = response.data.access;
              console.log("token refreshed");
              axios.defaults.headers[
                "Authorization"
              ] = `JWT ${response.data.access}`;
              originalRequest.headers[
                "Authorization"
              ] = `JWT ${response.data.access}`;
              // TODO: set current user logic goes here
              return axios(originalRequest);
            })
            .catch((err) => {
              console.log(err);
            });
        } else {
          console.log("Refresh token is expired", tokenParts.exp, now);
          alert("Token has Expired you need to login again");
          // TODO: trigger login again logic here
        }
      } else {
        console.log("Refresh token not available.");
        // TODO: trigger login again logic here
      }
    }

    return Promise.reject(error);
  }
);

export default axios;
