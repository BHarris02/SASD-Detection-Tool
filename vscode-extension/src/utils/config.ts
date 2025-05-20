/**
 * Module Name: config.ts
 * Description: This module provides configuration settings for the application.
 *              It defines and exports the BASE_API_URL by reading the environment variable 
 *              'BASE_API_URL' or defaulting to 'http://127.0.0.1:5000/api' if not set
 * Author: Blake Harris (bharris06@qub.ac.uk)
 * Version: 1.0.0
 * License: MIT License
 * Dependencies: 
 * Usage:
 *    Import this module wherever you need to use the BASE_API_URL:
 *       import config from './config';
 */
const BASE_API_URL = process.env.BASE_API_URL || 'http://127.0.0.1:5000/api';

export default {
    BASE_API_URL,
};