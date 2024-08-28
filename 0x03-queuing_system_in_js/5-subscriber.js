const redis = require('redis');

// Create Redis client
const subscriber = redis.createClient();

// Handle connection events
subscriber.on('connect', () => {
    console.log('Redis client connected to the server');
});

subscriber.on('error', (err) => {
    console.error('Redis client not connected to the server:', err.message);
});

// Subscribe to the 'holberton school channel'
subscriber.subscribe('holberton school channel');

// Handle receiving messages on the channel
subscriber.on('message', (channel, message) => {
    console.log(`Received message: ${message}`);
    if (message === 'KILL_SERVER') {
        subscriber.unsubscribe('holberton school channel');
        subscriber.quit();
    }
});
