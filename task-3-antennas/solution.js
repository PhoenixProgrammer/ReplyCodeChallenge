const argv = require('minimist')(process.argv.slice(2))

let _ = require("lodash")
let fs = require("fs")

if(argv.f) {
    fs.readFile(argv.f, "utf-8", (err, data) => {
        if(err) {
            console.error("Couldnt read file: " + err)
        } else {
            let content = data.toString("utf-8")

            console.log("Content: " + content)

            let lines = _.split(content, "\n")

            let tests = []

            for(let i = 1; i < lines.length - 1; i += 3) {

                let noAntennas
                let noToDeploy

                let antennaScores
                let buildingScores

                for(let j = 0; j < 3; j++) {
                    if(j == 0) {
                        let meta = _.split(lines[i], " ")
                        noAntennas = meta[0]
                        noToDeploy = meta[1]
                    }

                    if(j == 1) {
                        antennaScores = _.split(lines[i + 1], " ")
                    }

                    if(j == 2) {
                        buildingScores = _.split(lines[i + 2], " ")
                    }
                }

                tests.push({
                    noAntennas: noAntennas,
                    noToDeploy: noToDeploy,
                    antennaScores: antennaScores,
                    buildingScores: buildingScores
                })
            }

            //lets do voodoo magic

            let results = []

            tests.forEach((test) => {
                let min = 0
                let max = 0
    
                //pick extremum score
                let maxBuildings = extremumInArray(test.buildingScores, test.noToDeploy, true)
                let maxAntennas = extremumInArray(test.antennaScores, test.noToDeploy, true)

                let minBuildings = extremumInArray(test.buildingScores, test.noToDeploy, false)
                let minAntennas = extremumInArray(test.antennaScores, test.noToDeploy, false)

                //get max score
                for(let i = 0; i < maxBuildings.length; i++) {
                    max += maxBuildings[i] * maxAntennas[i]
                }

                //get min score
                for(let i = 0; i < minBuildings.length; i++) {
                    min += minBuildings[i] * minAntennas[i]
                }

                results.push({
                    min: min,
                    max: max
                })
            })

            console.log(results)

            let output = ""

            /*for(let i = 0; i < tests.length; i++) {
                output += "Case #" + (i + 1) + ": "
                tests[i].finalConfig.forEach((n) => {
                    output += n + " "
                })

                output += "\r\n"
            }

            console.log(output)

            fs.writeFile(argv.o, output, {encoding: "ascii"}, (err) => {
                if(err) {
                    console.error("Cant write the file")
                }
            })*/
        }
    })
} else {
    console.error("no file path specified")
}

function extremumInArray(arr_org, no, maximum) {

    let arr = _.clone(arr_org)

    let extr = []

    for(let i = 0; i < no; i++) {

        let tmpExtrIndex = 0

        for(let j = 0; j < arr.length; j++) {
            if(maximum) {
                if(arr[tmpExtrIndex] < arr[j]) {
                    tmpExtrIndex = j
                }
            } else {
                if(arr[tmpExtrIndex] > arr[j]) {
                    tmpExtrIndex = j
                }
            }
        }

        extr.push(arr[tmpExtrIndex])

        arr.splice(tmpExtrIndex, 1)
    }

    return extr
}