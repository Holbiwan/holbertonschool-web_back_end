// Importing necessary functions from external modules
import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

// Define an asynchronous function 'handleProfileSignup'
async function handleProfileSignup(firstName, lastName, fileName) {
  // Helper function to create and handle promises
  const createPromise = async (promise, asyncFn) => {
    try {
      // Try to await the asynchronous function
      promise.value = await asyncFn();
      promise.status = 'fulfilled';
    } catch (err) {
      // If there's an error, handle it and mark the promise as rejected
      promise.value = err.toString();
      promise.status = 'rejected';
    }
  };

  // Define two promises with 'pending' status
  const promise1 = { status: 'pending' };
  const promise2 = { status: 'pending' };

  // Create promises for signUpUser and uploadPhoto functions
  await createPromise(promise1, () => signUpUser(firstName, lastName));
  await createPromise(promise2, () => uploadPhoto(fileName));

  // Return an array containing the results of both promises
  return [promise1, promise2];
}

// Export the 'handleProfileSignup' function as the default export
export default handleProfileSignup;
