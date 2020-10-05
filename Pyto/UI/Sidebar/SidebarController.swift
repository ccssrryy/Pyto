//
//  SidebarController.swift
//  Pyto
//
//  Created by Adrian Labbé on 08-09-20.
//  Copyright © 2020 Adrian Labbé. All rights reserved.
//

import SwiftUI

@available(iOS 14.0, *)
class SidebarController: UIHostingController<AnyView> {
    
    private var sceneDelegate: SceneDelegate?
    
    override var childForHomeIndicatorAutoHidden: UIViewController? {
        guard let scene = view.window?.windowScene else {
            return nil
        }
        
        guard let editor = EditorView.EditorStore.perScene[scene]?.editor else {
            return nil
        }
        
        guard editor.viewController?.view.window != nil else {
            return nil
        }
        
        return editor.viewController
    }
    
    override func viewDidAppear(_ animated: Bool) {
        super.viewDidAppear(animated)
        
        sceneDelegate = view.window?.windowScene?.delegate as? SceneDelegate
    }
    
    override func viewDidDisappear(_ animated: Bool) {
        super.viewDidDisappear(animated)
        
        if presentedViewController == nil {
            sceneDelegate?.sceneStateStore.reset()
            sceneDelegate = nil
        }
    }
}
