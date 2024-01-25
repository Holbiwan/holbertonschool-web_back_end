export default function handleResponseFromAPI(promise) {
    return promise
      .then(() => {
        console.log('Got a response from the API');
        return { status: 200, body: 'success' };
      })
      .catch(() => {
        console.log('Got a response from the API');
        throw new Error(); // Utilisez 'throw' pour rejeter la promesse avec une erreur
      });
  }
  