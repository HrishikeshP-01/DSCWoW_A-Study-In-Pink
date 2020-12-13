let $=require('jquery')
let fs = require('fs')
const {spawn} = require('child_process')

$('#GenMap').on('click',()=>{
    let datasetName = $('#myfile').val()
    let epsilon = $('#epsilon').val()
    let maxDist = $('#MaxDist').val()


fs.writeFile('META.txt',datasetName+"\n"+maxDist+"\n"+epsilon,(err)=>{
    if(err){
        console.log(err)
    }
})

const python = spawn('python',['PythonBackend.py'])

outputMapFileName='JustForDemo.html'

reDirect(outputMapFileName)
})

function reDirect(outputMapFileName){
    fs.access(outputMapFileName,fs.constants.F_OK,(err)=>{
        if(err){
            setTimeout(1000)
            reDirect(outputMapFileName)
        }
        if(!err){
            window.location.replace(outputMapFileName)
        }
    })
}