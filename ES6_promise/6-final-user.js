import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

async function handleProfileSignup(firstName, lastName, fileName) {
  const createPromise = async (promise, asyncFn) => {
    try {
      promise.value = await asyncFn();
      promise.status = 'fulfilled';
    } catch (err) {
      promise.value = err.toString();
      promise.status = 'rejected';
    }
  };

  const promise1 = { status: 'pending' };
  const promise2 = { status: 'pending' };

  await createPromise(promise1, () => signUpUser(firstName, lastName));
  await createPromise(promise2, () => uploadPhoto(fileName));

  return [promise1, promise2];
}

export default handleProfileSignup;
