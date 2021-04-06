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

            for(let i = 1; i < lines.length - 2; i += 2) {

                let noSeat
                let noDays

                let exConfig

                for(let j = 0; j < 2; j++) {
                    if(j == 0) {
                        let meta = _.split(lines[i], " ")
                        noSeat = meta[0]
                        noDays = meta[1]
                    }

                    if(j == 1) {
                        exConfig = _.split(lines[i + 1], " ")
                    }
                }

                let finalConfig = []

                for(let i = 0; i < noSeat; i++) {
                    finalConfig.push(i)
                }

                tests.push({
                    noSeat: noSeat,
                    noDays: noDays,
                    exConfig: exConfig,
                    finalConfig: finalConfig
                })
            }

            //iterate over every test
            tests.forEach((test) => {

                //step over every day
                for(let i = 0; i < test.noDays; i++) {

                    //go over every person
                    let frozenConfig = _.clone(test.finalConfig)

                    for(let j = 0; j < test.finalConfig.length; j++) {
                        let person = frozenConfig[j]

                        let nextSeat = test.exConfig[j]

                        test.finalConfig[nextSeat] = person
                    }
                }
            })

            let output = ""

            for(let i = 0; i < tests.length; i++) {
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
            })
        }
    })
} else {
    console.error("no file path specified")
}