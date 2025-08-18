const URL = 'https://meowfacts.herokuapp.com';

(async (URL) => {
    try {
        const response = await fetch(URL);
        const data = await response.json();
        console.log("Fetched random fact: ", data?.data);

    } catch (error) {
        console.log("Something went wrong!!!");

    }
})(URL);
