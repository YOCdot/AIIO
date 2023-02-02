let jws = require("jws");


function jwt_generate(payload, secret = null, header = null) {

    if (header === null) {
        header = {
            "typ": "jwt",
            "alg": "HS256"
        }
    }

    return jws.sign({
        header: header,
        payload: payload,
        secret: secret
    })

}

// let signature = jwt_generate(
//     {
//         "name": "yoc",
//         "password": "jwt",
//         "exp": 1674745736
//     },
//     "django-insecure-pz+e98#%pf=v=ctr3(xc6&$@($-m_7-@c!tzym!qkoh(&*7bfc"
// )
// console.log(signature)

export {jwt_generate};
