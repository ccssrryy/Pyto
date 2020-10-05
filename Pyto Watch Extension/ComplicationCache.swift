//
//  ComplicationCache.swift
//  Pyto Watch Extension
//
//  Created by Adrian Labbé on 05-10-20.
//  Copyright © 2020 Adrian Labbé. All rights reserved.
//

import WatchKit
import WatchConnectivity

class ComplicationCache {
    
    var cachedTimeline = [PyComplication]() {
        didSet {
            WCSession.default.sendMessage(["Set": "cachedTimeline"], replyHandler: nil, errorHandler: nil)
            if let date = sortedTimeline.first?.date {
                WCSession.default.sendMessage(["Schedule Background Task": date], replyHandler: nil, errorHandler: nil)
                
                WKExtension.shared().scheduleBackgroundRefresh(withPreferredDate: date, userInfo: nil) { (error) in
                    if let error = error {
                        WCSession.default.sendMessage(["Error": error.localizedDescription], replyHandler: nil, errorHandler: nil)
                    }
                }
            }
        }
    }
    
    var sortedTimeline: [PyComplication] {
        return cachedTimeline.sorted { (a, b) -> Bool in
            guard let aDate = a.date else {
                return false
            }
            
            guard let bDate = a.date else {
                return true
            }
            
            return aDate > bDate
        }.reversed()
    }
}
