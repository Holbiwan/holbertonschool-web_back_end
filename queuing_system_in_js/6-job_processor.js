import kue from 'kue';

// Create the queue
const queue = kue.createQueue();

const queueName = 'push_notification_code';

const sendNotification = (phoneNumber, message) => {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
};

queue.process(queueName, (job, done) => {
  const { phoneNumber, message } = job.data;

  try {
    sendNotification(phoneNumber, message);
    done(); // Signal job completion success
  } catch (error) {
    console.error(`Failed to send notification: ${error.message}`);
    done(error); // Signal job completion with error
  }
});
