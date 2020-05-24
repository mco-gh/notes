zzarcon/react-circle

###    README.md

 [![demo.gif](../_resources/200bda59e697af0e4ed6da66f40c913b.gif)](https://github.com/zzarcon/react-circle/blob/master/demo.gif)

# [(L)](https://github.com/zzarcon/react-circle#react-circle-)react-circle [[68747470733a2f2f7472617669732d63692e6f72672f7a7a6172636f6e2f72656163742d636972636c652e7376673f6272616e63683d6d6173746572](../_resources/af3359b6a330e8be6d21e0274c77bc30.bin)](https://travis-ci.org/zzarcon/react-circle)

> Renders a svg circle + percentage. It just works

# [(L)](https://github.com/zzarcon/react-circle#demo)Demo

[https://zzarcon.github.io/react-circle](https://zzarcon.github.io/react-circle/)

# [(L)](https://github.com/zzarcon/react-circle#install-)Install

	$ yarn add react-circle

# [(L)](https://github.com/zzarcon/react-circle#usage-)Usage ⛏

**Basic**

ReactCircle is opinionated and comes with default size and colors, just pass the **progress** prop to get them:

import  Circle  from  'react-circle';<Circle
progress={35}/>
**Custom**
Optionally, you can pass the following props and customize it as your will

import  Circle  from  'react-circle';// All avaliable props for customization:// Details are ordered as:// <Type>: <Description><Circle

animate={true} // Boolean: Animated/Static progress responsive={true} // Boolean: Make SVG adapt to parent size size={150} // Number: Defines the size of the circle. lineWidth={14} // Number: Defines the thickness of the circle's stroke.  progress={69} // Number: Update to change the progress and percentage. progressColor="cornflowerblue"  // String: Color of "progress" portion of circle. bgColor="whitesmoke"  // String: Color of "empty" portion of circle. textColor="hotpink"  // String: Color of percentage text color. textStyle={{ font:  'bold 5rem Helvetica, Arial, sans-serif'  // CSSProperties: Custom styling for percentage. }}

percentSpacing={10} // Number: Adjust spacing of "%" symbol and number. roundedStroke={true} // Boolean: Rounded/Flat line ends showPercentage={true} // Boolean: Show/hide percentage. showPercentageSymbol={true} // Boolean: Show/hide only the "%" symbol./>