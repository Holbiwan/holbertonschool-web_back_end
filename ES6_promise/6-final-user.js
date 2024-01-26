// Importing necessary functions from external modules
import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

// Define an asynchronous function 'handleProfileSignup'
async function handleProfileSignup(firstName, lastName, fileName) {
    // Helper function to create a promise
  const createPromise = async (promise, asyncFn) => {
    try {
        // Try to await the asynchronous function
      promise.value = await asyncFn();
      promise.status = 'fulfilled';
    } catch (err) {
        // If the asynchronous function throws an error, catch it
      promise.value = err.toString();
      promise.status = 'rejected';
    }
  };

  // Create two promises
  const promise1 = { status: 'pending' };
  const promise2 = { status: 'pending' };

  // Await the asynchronous functions
  await createPromise(promise1, () => signUpUser(firstName, lastName));
  await createPromise(promise2, () => uploadPhoto(fileName));

    // Return the promises
  return [promise1, promise2];
}

// Export the function 'handleProfileSignup'
export default handleProfileSignup;
