import redis from 'redis';

// Create the Redis client
const client = redis.createClient();

const CHANNEL = 'holberton school channel';

// Handle connection errors
client.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error.message}`);
});

// Confirm connection and subscribe to channel
client.on('connect', () => {
  console.log('Redis client connected to the server');
  client.subscribe(CHANNEL, (err) => {
    if (err) {
      console.error(`Failed to subscribe to ${CHANNEL}: ${err.message}`);
    } else {
      console.log(`Subscribed to ${CHANNEL}`);
    }
  });
});

// Handle incoming messages
client.on('message', (channel, message) => {
  console.log(`Message from ${channel}: ${message}`);

  if (message === 'KILL_SERVER') {
    client.unsubscribe(CHANNEL, (err) => {
      if (err) {
        console.error(`Failed to unsubscribe from ${CHANNEL}: ${err.message}`);
      } else {
        console.log(`Unsubscribed from ${CHANNEL}`);
      }
    });
    client.quit(() => {
      console.log('Redis client connection closed');
    });
  }
});
