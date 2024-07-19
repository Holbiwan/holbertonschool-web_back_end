import kue from 'kue';

const queue = kue.createQueue();
const queueName = 'push_notification_code_2';

const blacklisted = ['4153518780', '4153518781'];

const sendNotification = (phoneNumber, message, job, done) => {
  const total = 100;
  job.progress(0, total, () => {
    if (blacklisted.includes(phoneNumber)) {
      const error = new Error(`Phone number ${phoneNumber} is blacklisted`);
      console.error(error.message);
      done(error);
      return;
    }

    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    job.progress(50, total, () => {
      // Simulate successful notification sending
      job.progress(100, total, () => {
        done(); // Signal successful completion of the job
      });
    });
  });
};

queue.process(queueName, 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});
