

var chart_config = [];
var dynamicDataInverter = [[121.312,120.21,156],[56.12,21.42,43],[321.50, 20, 310.12]];
var dynamicDataBattery = [[],[],[]];
var dynamicDataGenerator = [[],[],[]]
function chartBuilder(nodes, generators, inverters, batteries){
    chart_config = {
        chart: {
            container: "#custom-colored",

            nodeAlign: "BOTTOM",

            connectors: {
                type: 'step'
            },
            node: {
                HTMLclass: 'nodeExample1'
            }
        },nodeStructure: {
            text: {
                name: "Transformer-1",
                title: "Location : ASU-Poly",
                contact: "Type : Transformer"
            },
            image: "/static/assets/transformer.png",
            HTMLclass: 'light-gray',
            children: []
                }
        };
    for (var i =0; i < nodes.length; i++){
        var childOfEMS = { text: {
            name: nodes[i].fields.object_id,
            title: "Node",
            manufacturer: "Manufacturer : "+nodes[i].fields.manufacturer,
            model: "Model : "+nodes[i].fields.model
        },
            image: "/static/assets/pi.png",
            HTMLclass: 'gray',
            children: []
        };

        //Add generator child nodes
        for (var device1 =0; device1 < generators.length; device1++){
            if (generators[device1].fields.nc_id == nodes[i].fields.object_id){

                var generator_node = { text: {
                    name: generators[device1].pk,
                    manufacturer: "Manufacturer : "+ generators[device1].fields.manufacturer,
                    contact: "Type : Generator",
                    title: "Output Volts: " + dynamicDataInverter[randomNumber()][randomNumber()],
                    model: "Input Volts: " + dynamicDataInverter[randomNumber()][randomNumber()],
                    frequency: "Frequency : " + dynamicDataInverter[randomNumber()][randomNumber()]
                    },
                    link: {
                        href: "http://127.0.0.1:8000/generator/",
                        target: "_blank"
                     },
                    image: "/static/assets/generator.png",
                    HTMLclass: 'red'
                };
                childOfEMS.children.push(generator_node);
            }
        }
        //Add battery child nodes
        for (var device2 =0; device2 < batteries.length; device2++){
            if (batteries[device2].fields.nc_id == nodes[i].fields.object_id){
                var battery_node = { text: {
                    name: batteries[device2].pk,
                    manufacturer: "Manufacturer : "+ batteries[device2].fields.manufacturer,
                    contact: "Type : Battery",
                    title: "Output Volts: " + dynamicDataInverter[randomNumber()][randomNumber()],
                    model: "Input Volts: " + dynamicDataInverter[randomNumber()][randomNumber()],
                    frequency: "Frequency : " + dynamicDataInverter[randomNumber()][randomNumber()]
                    },
                    link: {
                        href: "http://127.0.0.1:8000/battery/",
                        target: "_blank"
                     },
                    image: "/static/assets/battery.png",
                    HTMLclass: 'blue'
                };
                childOfEMS.children.push(battery_node);
            }
        }
        //Add inverter child nodes
        for (var device3 =0; device3 < inverters.length; device3++){
            if (inverters[device3].fields.nc_id == nodes[i].fields.object_id){
                var inverter_node = { text: {
                    name: inverters[device3].pk,
                    manufacturer: "Manufacturer : "+ inverters[device3].fields.manufacturer,
                    contact: "Type : Inverter",
                    title: "Output Volts: " + dynamicDataInverter[randomNumber()][randomNumber()],
                    model: "Input Volts: " + dynamicDataInverter[randomNumber()][randomNumber()],
                    frequency: "Frequency : " + dynamicDataInverter[randomNumber()][randomNumber()]
                    },
                    link: {
                        href: "http://127.0.0.1:8000/inverter/",
                        target: "_blank"
                     },
                    image: "/static/assets/inverter.png",
                    HTMLclass: 'green'
                };
                childOfEMS.children.push(inverter_node);
            }
        }
        chart_config.nodeStructure.children.push(childOfEMS);
    }

}
var i=0;
function hello() {
    i++;
    console.log(i);
}

function randomNumber() {
    return Math.floor((Math.random() * 3));
}

