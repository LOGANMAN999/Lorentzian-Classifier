# Lorentzian classifier
This algorithm was created by jdehorty (Justin Dehorty) in Trading View. This is a python implementation that is connected to a web socket channel of the American Crypto Currency exchange Kraken. This algorithm is paired with a portfolio class which allows you to record your entries and exits, change simulated leverage, and calculate profits. This python implementation is meant to be expanded upon to allow for furhter customization and testing. This algorithm uses a non-euclidean metric space to calculate distances between points (candles) in an n-dimensional metric spaces, where n is the number of features or technical indicators used, and our metric is the lorentzian distance. Here is an excerpt from jdehorty's trading view comments:

// When using Machine Learning algorithms like K-Nearest Neighbors, choosing an
// appropriate distance metric is essential. Euclidean Distance is often used as
// the default distance metric, but it may not always be the best choice. This is
// because market data is often significantly impacted by proximity to significant
// world events such as FOMC Meetings and Black Swan events. These major economic
// events can contribute to a warping effect analogous a massive object's 
// gravitational warping of Space-Time. In financial markets, this warping effect 
// operates on a continuum, which can analogously be referred to as "Price-Time".

// To help to better account for this warping effect, Lorentzian Distance can be
// used as an alternative distance metric to Euclidean Distance. The geometry of
// Lorentzian Space can be difficult to visualize at first, and one of the best
// ways to intuitively understand it is through an example involving 2 feature
// dimensions (z=2). For purposes of this example, let's assume these two features
// are Relative Strength Index (RSI) and the Average Directional Index (ADX). In
// reality, the optimal number of features is in the range of 3-8, but for the sake
// of simplicity, we will use only 2 features in this example.

// Fundamental Assumptions:
// (1) We can calculate RSI and ADX for a given chart.
// (2) For simplicity, values for RSI and ADX are assumed to adhere to a Gaussian 
//     distribution in the range of 0 to 100.
// (3) The most recent RSI and ADX value can be considered the origin of a coordinate 
//     system with ADX on the x-axis and RSI on the y-axis.

// Distances in Euclidean Space:
// Measuring the Euclidean Distances of historical values with the most recent point
// at the origin will yield a distribution that resembles Figure 1 (below).

//                        [RSI]
//                          |                      
//                          |                   
//                          |                 
//                      ...:::....              
//                .:.:::••••••:::•::..             
//              .:•:.:•••::::••::••....::.            
//             ....:••••:••••••••::••:...:•.          
//            ...:.::::::•••:::•••:•••::.:•..          
//            ::•:.:•:•••••••:.:•::::::...:..         
//  |--------.:•••..•••••••:••:...:::•:•:..:..----------[ADX]    
//  0        :•:....:•••••::.:::•••::••:.....            
//           ::....:.:••••••••:•••::••::..:.          
//            .:...:••:::••••••••::•••....:          
//              ::....:.....:•::•••:::::..             
//                ..:..::••..::::..:•:..              
//                    .::..:::.....:                
//                          |            
//                          |                   
//                          |
//                          |
//                         _|_ 0        
//                          
//        Figure 1: Neighborhood in Euclidean Space

// Distances in Lorentzian Space:
// However, the same set of historical values measured using Lorentzian Distance will 
// yield a different distribution that resembles Figure 2 (below).

//                         
//                         [RSI] 
//  ::..                     |                    ..:::  
//   .....                   |                  ......
//    .••••::.               |               :••••••. 
//     .:•••••:.             |            :::••••••.  
//       .•••••:...          |         .::.••••••.    
//         .::•••••::..      |       :..••••••..      
//            .:•••••••::.........::••••••:..         
//              ..::::••••.•••••••.•••••••:.            
//                ...:•••••••.•••••••••::.              
//                  .:..••.••••••.••••..                
//  |---------------.:•••••••••••••••••.---------------[ADX]          
//  0             .:•:•••.••••••.•••••••.                
//              .••••••••••••••••••••••••:.            
//            .:••••••••••::..::.::••••••••:.          
//          .::••••••::.     |       .::•••:::.       
//         .:••••••..        |          :••••••••.     
//       .:••••:...          |           ..•••••••:.   
//     ..:••::..             |              :.•••••••.   
//    .:•....                |               ...::.:••.  
//   ...:..                  |                   :...:••.     
//  :::.                     |                       ..::  
//                          _|_ 0
//
//       Figure 2: Neighborhood in Lorentzian Space 


// Observations:
// (1) In Lorentzian Space, the shortest distance between two points is not 
//     necessarily a straight line, but rather, a geodesic curve.
// (2) The warping effect of Lorentzian distance reduces the overall influence  
//     of outliers and noise.
// (3) Lorentzian Distance becomes increasingly different from Euclidean Distance 
//     as the number of nearest neighbors used for comparison increases.

