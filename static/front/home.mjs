export default {
    async login() {
        const cred = {
            username: "1",
        }
        const x = await fetch("/api/users/login/", {
            method: "POST",
            headers: {
                'Content-Type': 'application/json; charset=UTF-8', // Declare the content type
            },
            body: JSON.stringify(cred)
        });
        console.log(await x.text())
    }
}

