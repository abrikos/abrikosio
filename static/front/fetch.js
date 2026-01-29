const basePath = '/api'

function getCookie(name) {
    // Append "=" to the name to ensure we match the full cookie name
    const nameEQ = name + "=";
    // Split the document.cookie string by semicolon and space
    const ca = document.cookie.split('; ');

    // Loop through the cookie array
    for (let i = 0; i < ca.length; i++) {
        let c = ca[i];
        // Remove leading white space if it exists (though 'split('; ')' handles this)
        // while (c.charAt(0) === ' ') c = c.substring(1, c.length);

        // If the cookie string starts with the name we're looking for,
        // return its value (everything after the "=")
        if (c.indexOf(nameEQ) === 0) {
            // Use decodeURIComponent to handle special characters
            return decodeURIComponent(c.substring(nameEQ.length, c.length));
        }
    }
    return null; // Return null if the cookie is not found
}

function getHeaders() {
    const headers = {
        'Content-Type': 'application/json'
    }
    const access = getCookie('access');
    if(access){
        headers['Authorization'] = `Bearer ${access}`;
    }
    return headers;
}

async function fetch_over(method, path, data){
    const body = JSON.stringify(data)
    const res = await fetch(basePath + path, {method, body, headers: getHeaders()})
    if (!res.ok) {
        const error = await res.json()
        Quasar.Notify.create({message: error.detail || JSON.stringify(error), color: 'red'})
    } else {
        return res.json();
    }
}

export default {
    async get(path) {
        return  fetch_over('get',path);
    },
    async post(path, data) {
        return  fetch_over('post',path);
    },
}