let webApiSitios = 'http://localhost/apis/sitios_onair/'
let sitiosAUP = document.querySelectorAll('.counter')
let detallesArg = document.querySelectorAll('.counterARG')
let detallesUru = document.querySelectorAll('.counterURU')
let detallesPar = document.querySelectorAll('.counterPAR')
let tecnoArg = document.querySelectorAll('.tecnoARG')
let tecnoUru = document.querySelectorAll('.tecnoURU')
let tecnoPar = document.querySelectorAll('.tecnoPAR')


fetch(webApiSitios)
    .then(res => {
        console.log('Response, waiting to parse..')
        return res.json()
    })
    .then(data => {
        console.log('Data parsed..', data)
        let finalData = data
        sitiosAUP[0].textContent = finalData[0].SITIOS
        sitiosAUP[1].textContent = finalData[2].SITIOS
        sitiosAUP[2].textContent = finalData[1].SITIOS

        detallesArg[0].textContent = finalData[0].MACRO
        detallesArg[1].textContent = finalData[0].STREETCELL
        detallesArg[2].textContent = finalData[0].INDOOR
        detallesUru[0].textContent = finalData[2].MACRO
        detallesUru[1].textContent = finalData[2].STREETCELL
        detallesUru[2].textContent = finalData[2].INDOOR
        detallesPar[0].textContent = finalData[1].MACRO
        detallesPar[1].textContent = finalData[1].STREETCELL
        detallesPar[2].textContent = finalData[1].INDOOR
		
		tecnoArg[0].textContent = finalData[0].G2
        tecnoArg[1].textContent = finalData[0].G3
        tecnoArg[2].textContent = finalData[0].G4
        tecnoUru[0].textContent = finalData[2].G2
        tecnoUru[1].textContent = finalData[2].G3
        tecnoUru[2].textContent = finalData[2].G4
        tecnoPar[0].textContent = finalData[1].G2
        tecnoPar[1].textContent = finalData[1].G3
        tecnoPar[2].textContent = finalData[1].G4
    })
    .catch(e => {
        console.log(e)
    })


// let G5 = 'http://localhost/apis/G5/'

// fetch(G5)
//     .then(res => {
//         console.log('Response, waiting to parse..')
//         return res.json()
//     })
//     .then(data => {
//         console.log('Data parsed..', data)
//         let finalData = data
//         tecnoArg[3].textContent = finalData[0].NR_5G
//         tecnoArg[4].textContent = finalData[0].DSS_5G
//         tecnoPar[3].textContent = finalData[1].NR_5G
//         tecnoPar[4].textContent = finalData[1].DSS_5G
//         // tecnoUru[3].textContent = finalData[2].NR_5G
//         // tecnoUru[4].textContent = finalData[2].DSS_5G
//         tecnoUru[3].textContent = 2
//         tecnoUru[4].textContent = 3
//     })
//     .catch(e => {
//         console.log(e)
//     })


// let webApiPob = 'http://localhost/apis/poblacion_cubierta/'
// let pobARG = document.querySelectorAll('.pobARG')
// let pobURU = document.querySelectorAll('.pobURU')
// let pobPAR = document.querySelectorAll('.pobPAR')
    
// fetch(webApiPob)
//     .then(res => {
//         console.log('Response, waiting to parse..')
//         return res.json()
//     })
//     .then(data => {
//         console.log('Data parsed..', data)
//         let finalData = data
//         pobARG[0].textContent = finalData[0].CIUDADES_TOTAL
//         pobARG[1].textContent = `${(100-(finalData[0].CIUDADES_SC/finalData[0].CIUDADES_TOTAL)*100).toFixed(2)}%`
//         pobARG[2].textContent = `${(100-(finalData[0].POBLACION_SC/finalData[0].POBLACION_TOTAL)*100).toFixed(2)}%`

//         pobURU[0].textContent = finalData[1].CIUDADES_TOTAL
//         pobURU[1].textContent = `${(100-(finalData[1].CIUDADES_SC/finalData[1].CIUDADES_TOTAL)*100).toFixed(2)}%`
//         pobURU[2].textContent = `${(100-(finalData[1].POBLACION_SC/finalData[1].POBLACION_TOTAL)*100).toFixed(2)}%`

//         pobPAR[0].textContent = finalData[2].CIUDADES_TOTAL
//         pobPAR[1].textContent = `${(100-(finalData[2].CIUDADES_SC/finalData[2].CIUDADES_TOTAL)*100).toFixed(2)}%`
//         pobPAR[2].textContent = `${(100-(finalData[2].POBLACION_SC/finalData[2].POBLACION_TOTAL)*100).toFixed(2)}%`
//     })
//     .catch(e => {
//         console.log(e)
//     })