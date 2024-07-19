import kue from 'kue';

// Create the queue
const queue = kue.createQueue();

// Define the job data
const objectJob = {
  phoneNumber: '3167308713',
  message: 'This is the code to verify your account',
};

// Define the queue name
const queueName = 'push_notification_code';

// Create and save the job
queue.create(queueName, objectJob).save((err, job) => {
  if (err) {
    console.error(`Failed to create notification job: ${err}`);
  } else {
    console.log(`Notification job created: ${job.id}`);

    // Attach event listeners within the save callback
    job.on('complete', () => {
      console.log('Notification job completed');
    }).on('failed', (errorMessage) => {
      console.log(`Notification job failed: ${errorMessage}`);
    }).on('progress', (progress) => {
      console.log(`Notification job ${job.id} ${progress}% complete`);
    });
  }
});
