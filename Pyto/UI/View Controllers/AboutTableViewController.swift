//
//  AboutTableViewController.swift
//  Pyto
//
//  Created by Adrian Labbé on 1/17/19.
//  Copyright © 2019 Adrian Labbé. All rights reserved.
//

import UIKit
import SafariServices
import MessageUI
import NotificationCenter
import WatchConnectivity

fileprivate extension IndexPath {
    
    static let theme = IndexPath(row: 0, section: 0)
    static let indentation = IndexPath(row: 1, section: 0)
    static let fontSize = IndexPath(row: 2, section: 0)
    static let font = IndexPath(row: 3, section: 0)
    static let showConsoleAtBottom = IndexPath(row: 4, section: 0)
    static let showSeparator = IndexPath(row: 5, section: 0)
    
    static let todayWidget = IndexPath(row: 0, section: 1)
    
    static let downloadAll = IndexPath(row: 0, section: 2)
    
    static let watchScript = IndexPath(row: 0, section: 3)
    static let inputSugestions = IndexPath(row: 1, section: 3)
    
    static let discord = IndexPath(row: 0, section: 5)
    static let contact = IndexPath(row: 1, section: 5)
    
    static let acknowledgments = IndexPath(row: 0, section: 6)
    static let sourceCode = IndexPath(row: 1, section: 6)
}

/// A View controller with settings and info.
class AboutTableViewController: UITableViewController, UIDocumentPickerDelegate, MFMailComposeViewControllerDelegate, UIFontPickerViewControllerDelegate {
    
    private var lastIndex: IndexPath?
    
    /// Closes this View controller.
    @IBAction func close(_ sender: Any) {
        if #available(iOS 13.0, *) {
            if navigationController?.presentingViewController != nil {
                dismiss(animated: true, completion: nil)
            } else if let sceneSession = view.window?.windowScene?.session {
                UIApplication.shared.requestSceneSessionDestruction(sceneSession, options: nil, errorHandler: nil)
            }
        } else if navigationController?.presentingViewController != nil {
            dismiss(animated: true, completion: nil)
        }
    }
    
    /// Called when indentation is set.
    @IBAction func indentationChanged(_ sender: UISegmentedControl) {
        switch sender.selectedSegmentIndex {
        case 0:
            EditorViewController.indentation = "\t"
        case 1:
            EditorViewController.indentation = "  "
        case 2:
            EditorViewController.indentation = "    "
        case 3:
            EditorViewController.indentation = "      "
        case 4:
            EditorViewController.indentation = "        "
        default:
            EditorViewController.indentation = "  "
        }
    }
    
    /// The segmented control managing identation.
    @IBOutlet weak var identationSegmentedControl: UISegmentedControl!
    
    // MARK: - Font size
    
    /// The label previewing the font size.
    @IBOutlet weak var fontSizeLabel: UILabel!
    
    /// The stepper for setting font size.
    @IBOutlet weak var fontSizeStepper: UIStepper!
    
    /// Increases or dicreases font size.
    @IBAction func changeFontSize(_ sender: UIStepper) {
        ThemeFontSize = Int(sender.value)
        let label = fontSizeLabel
        let superview = label?.superview
        let constraints = superview?.constraints
        label?.removeFromSuperview()
        label?.text = "\(ThemeFontSize)px"
        label?.font = fontSizeLabel.font.withSize(CGFloat(ThemeFontSize))
        superview?.addSubview(label!)
        superview?.removeConstraints(superview!.constraints)
        superview?.addConstraints(constraints!)
    }
    
    // MARK: - Show console at bottom

    /// Switch for toggling console at bottom.
    @IBOutlet weak var showConsoleAtBottom: UISwitch!
    
    /// Toggles console at bottom.
    @IBAction func toggleConsoleAtBottom(_ sender: UISwitch) {
        EditorSplitViewController.shouldShowConsoleAtBottom = sender.isOn
        #if !Xcode11
        if #available(iOS 14.0, *) {
            EditorView.EditorStore.perScene.removeAll()
        }
        #endif
    }
    
    // MARK: - Show separator
    
    /// Switch for toggling the separator between editor and console.
    @IBOutlet weak var showSeparator: UISwitch!
    
    /// Toggles the separator between editor and console.
    @IBAction func toggleSeparator(_ sender: UISwitch) {
        EditorSplitViewController.shouldShowSeparator = sender.isOn
        #if !Xcode11
        if #available(iOS 14.0, *) {
            EditorView.EditorStore.perScene.removeAll()
        }
        #endif
    }
        
    // MARK: - Table view controller
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        title = navigationItem.title
        
        switch EditorViewController.indentation {
        case "\t":
            identationSegmentedControl.selectedSegmentIndex = 0
        case "  ":
            identationSegmentedControl.selectedSegmentIndex = 1
        case "    ":
            identationSegmentedControl.selectedSegmentIndex = 2
        case "      ":
            identationSegmentedControl.selectedSegmentIndex = 3
        case "        ":
            identationSegmentedControl.selectedSegmentIndex = 4
        default:
            identationSegmentedControl.selectedSegmentIndex = 0
        }
        
        fontSizeStepper.value = Double(ThemeFontSize)
        fontSizeLabel.text = "\(ThemeFontSize)px"
        fontSizeLabel.font = EditorViewController.font.withSize(CGFloat(ThemeFontSize))
        showConsoleAtBottom.isOn = EditorSplitViewController.shouldShowConsoleAtBottom
        showSeparator.isOn = EditorSplitViewController.shouldShowSeparator
        
        tableView.backgroundColor = .systemGroupedBackground
    }
    
    override func viewDidAppear(_ animated: Bool) {
        super.viewDidAppear(animated)
        
        if #available(iOS 13.0, *) {
            view.window?.windowScene?.title = navigationItem.title
        }
    }
    
    override func viewWillDisappear(_ animated: Bool) {
        super.viewWillDisappear(animated)
        
        if #available(iOS 13.0, *) {
            view.window?.windowScene?.title = ""
        }
    }
    
    override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        
        let cell = super.tableView(tableView, cellForRowAt: indexPath)
        
        if indexPath == .todayWidget {
            var isStale = false
            if let lastPathComponent = (UserDefaults.standard.string(forKey: "todayWidgetScriptPath") as NSString?)?.lastPathComponent {
                cell.detailTextLabel?.text = lastPathComponent
            } else if let data = UserDefaults.standard.data(forKey: "todayWidgetScriptPath"), let url = (try? URL(resolvingBookmarkData: data, bookmarkDataIsStale: &isStale)) {
                cell.detailTextLabel?.text = url.lastPathComponent
            } else {
                cell.detailTextLabel?.text = ""
            }
        } else if indexPath == .watchScript {
            var isStale = false
            if let data = UserDefaults.standard.data(forKey: "watchScriptPath"), let url = (try? URL(resolvingBookmarkData: data, bookmarkDataIsStale: &isStale)) {
                cell.detailTextLabel?.text = url.lastPathComponent
            } else {
                cell.detailTextLabel?.text = ""
            }
        } else if indexPath == .font {
            if #available(iOS 13.0, *) {
                cell.detailTextLabel?.text = EditorViewController.font.fontName
                cell.detailTextLabel?.font = EditorViewController.font
            } else {
                cell.contentView.alpha = 0.5
                cell.detailTextLabel?.text = "\(UIDevice.current.userInterfaceIdiom == .pad ? "iPadOS" : "iOS") 13+"
            }
        }
        
        if indexPath == .watchScript || indexPath == .inputSugestions {
            cell.isUserInteractionEnabled = WCSession.default.isPaired
            cell.contentView.alpha = WCSession.default.isPaired ? 1 : 0.5
        }
        
        return cell
    }
    
    override func tableView(_ tableView: UITableView, titleForFooterInSection section: Int) -> String? {
        let superFooter = super.tableView(tableView, titleForFooterInSection: section)
        
        if section == IndexPath.todayWidget.section {
            if #available(iOS 14.0, *) {
                return superFooter
            } else {
                return nil
            }
        } else {
            return superFooter
        }
    }
    
    override func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        
        lastIndex = indexPath
        
        let viewControllerToPresent: UIViewController?
        
        switch indexPath {
        case .theme:
            viewControllerToPresent = UIStoryboard(name: "Theme Chooser", bundle: Bundle.main).instantiateInitialViewController()
        case .font:
            if #available(iOS 13.0, *) {
                let config = UIFontPickerViewController.Configuration()
                config.includeFaces = true
                let fontPickerViewController = UIFontPickerViewController(configuration: config)
                fontPickerViewController.delegate = self
                viewControllerToPresent = fontPickerViewController
            } else {
                viewControllerToPresent = nil
            }
        case .todayWidget:
            let picker = UIDocumentPickerViewController(documentTypes: ["public.python-script"], in: .open)
            picker.delegate = self
            viewControllerToPresent = picker
        case .downloadAll:
            
            viewControllerToPresent = nil
            
            NSLog("Download")
            guard let script = Bundle.main.url(forResource: "download_all", withExtension: "py") else {
                NSLog("Nil")
                return
            }
            
            NSLog("Will present")
            let presenting = presentingViewController
            dismiss(animated: true) {
                let docBrowser = presenting?.presentingViewController as? DocumentBrowserViewController
                presenting?.dismiss(animated: true, completion: {
                    docBrowser?.openDocument(script, run: true)
                })
            }
        case .watchScript:
            let picker = UIDocumentPickerViewController(documentTypes: ["public.python-script"], in: .open)
            picker.delegate = self
            viewControllerToPresent = picker
        case .contact:
            let controller = MFMailComposeViewController()
            controller.setSubject("Pyto - Contact")
            controller.setToRecipients(["support@pyto.app"])
            controller.mailComposeDelegate = self
            viewControllerToPresent = controller
        case .discord:
            UIApplication.shared.open(URL(string: "https://discord.gg/326ster")!, options: [:], completionHandler: nil)
            viewControllerToPresent = nil
        case .acknowledgments:
            viewControllerToPresent = ThemableNavigationController(rootViewController: AcknowledgmentsViewController())
        case .sourceCode:
            viewControllerToPresent = SFSafariViewController(url: URL(string: "https://github.com/ColdGrub1384/Pyto")!)
        default:
            viewControllerToPresent = nil
        }
        
        tableView.deselectRow(at: indexPath, animated: true)
        
        guard let vc = viewControllerToPresent else {
            return
        }
        
        if indexPath == .theme || indexPath == .todayWidget {
            if vc is UIDocumentPickerViewController {
                present(vc, animated: true, completion: nil)
            } else {
                navigationController?.pushViewController(vc, animated: true)
            }
        } else {
            present(vc, animated: true, completion: nil)
        }
    }
    
    // MARK: - Document browser view controller delegate
    
    func documentPicker(_ controller: UIDocumentPickerViewController, didPickDocumentsAt urls: [URL]) {
        
        _ = urls[0].startAccessingSecurityScopedResource()
        
        navigationController?.popToRootViewController(animated: true)
        
        if lastIndex == IndexPath.watchScript {
            do {
                UserDefaults.standard.set(try urls[0].bookmarkData(), forKey: "watchScriptPath")
            } catch {
                print(error.localizedDescription)
            }
            UserDefaults.standard.synchronize()
            WCSession.default.transferCurrentComplicationUserInfo(["Reload":"All"])
        } else if lastIndex == IndexPath.todayWidget {
            do {
                UserDefaults.standard.set(try urls[0].bookmarkData(), forKey: "todayWidgetScriptPath")
            } catch {
                print(error.localizedDescription)
            }
            UserDefaults.standard.synchronize()
            (UIApplication.shared.delegate as? AppDelegate)?.copyModules()
            
            NCWidgetController().setHasContent(true, forWidgetWithBundleIdentifier: Bundle.main.bundleIdentifier!+".Pyto-Widget")
        }
        
        tableView.reloadData()
    }
    
    // MARK: - Mail compose view controller delegate
    
    func mailComposeController(_ controller: MFMailComposeViewController, didFinishWith result: MFMailComposeResult, error: Error?) {
        dismiss(animated: true) {
            if let error = error {
                let alert = UIAlertController(title: Localizable.error, message: error.localizedDescription, preferredStyle: .alert)
                alert.addAction(UIAlertAction(title: Localizable.cancel, style: .cancel, handler: nil))
                self.present(alert, animated: true, completion: nil)
            }
        }
    }
    
    // MARK: - Font picker view controller delegate
    
    @available(iOS 13.0, *)
    func fontPickerViewControllerDidPickFont(_ viewController: UIFontPickerViewController) {
        guard let fontDescriptor = viewController.selectedFontDescriptor else { return }
        let font = UIFont(descriptor: fontDescriptor, size: DefaultTheme().sourceCodeTheme.font.pointSize)
        EditorViewController.font = font
        
        tableView.reloadData()
        fontSizeLabel.font = EditorViewController.font.withSize(CGFloat(ThemeFontSize))
    }
}
