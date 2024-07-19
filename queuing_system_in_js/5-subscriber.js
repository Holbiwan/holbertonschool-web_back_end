import redis from 'redis';

const client = redis.createClient();

const CHANNEL = 'holberton school channel';

client.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error.message}`); // Use console.error for errors
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
  client.subscribe(CHANNEL, (err) => {
    if (err) {
      console.error(`Failed to subscribe to the channel: ${err.message}`);
    } else {
      console.log(`Subscribed to ${CHANNEL}`);
    }
  });
});

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
