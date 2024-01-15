export default function taskBlock(trueOrFalse) {
  const task = false;
  const task2 = true;

  // eslint-disable-next-line no-unused-vars
  if (trueOrFalse) {
    const localTask = true;
    const localTask2 = false;

    // eslint-disable-next-line no-unused-vars
    return [localTask, localTask2];
  }

  return [task, task2];
}
