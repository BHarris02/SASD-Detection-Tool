const config ={
    development: {
        API_BASE_URL: "http://backend:5000/api",
    },
    production: {
        API_BASE_URL: process.env.REACT_APP_API_BASE_URL,
    },
};

const ENV = process.env.NODE_ENV || "development";
export default config[ENV];