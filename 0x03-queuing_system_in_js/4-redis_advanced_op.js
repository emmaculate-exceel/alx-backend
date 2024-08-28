const redis = require('redis');

// Create a Redis client
const client = redis.createClient();

// Handle connection events
client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.on('error', (err) => {
    console.error('Redis error:', err);
});

// Store hash values
client.hset('HolbertonSchools', 'Portland', 50, redis.print);
client.hset('HolbertonSchools', 'Seattle', 80, redis.print);
client.hset('HolbertonSchools', 'New York', 20, redis.print);
client.hset('HolbertonSchools', 'Bogota', 20, redis.print);
client.hset('HolbertonSchools', 'Cali', 40, redis.print);
client.hset('HolbertonSchools', 'Paris', 2, redis.print);

// Retrieve and display the stored hash values
client.hgetall('HolbertonSchools', (err, result) => {
    if (err) {
        console.error('Error retrieving hash:', err);
        return;
    }
    console.log(result);
    client.quit(); // Close the Redis connection
});
