let $=require('jquery')
let fs = require('fs')


$('#GenMap').on('click',()=>{
    let datasetName = $('#myfile').val()
    let epsilon = $('#epsilon').val()
    let maxDist = $('#MaxDist').val()


fs.writeFile('META.txt',datasetName+"\n"+epsilon+"\n"+maxDist,(err)=>{
    if(err){
        console.log(err)
    }
})
})