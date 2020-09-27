//
//  FoldersBrowserViewController.swift
//  Pyto
//
//  Created by Adrian Labbé on 03-10-19.
//  Copyright © 2019 Adrian Labbé. All rights reserved.
//

import UIKit

/// A View controller for adding or removing folders that Pyto is allowed to read.
class FoldersBrowserViewController: UITableViewController, UIDocumentPickerDelegate {
    
    #if MAIN
    /// Folders readable and writable by Pyto.
    static var accessibleFolders: [URL] {
        set {
            var strings = [String]()
            
            for url in newValue {
                do {
                    strings.append((try url.bookmarkData()).base64EncodedString())
                } catch {
                    continue
                }
            }
            
            UserDefaults.standard.set(strings, forKey: "folders")
        }
        
        get {
            guard let urlsData = UserDefaults.standard.stringArray(forKey: "folders") else {
                return []
            }
            
            var urls = [URL]()
            
            for url in urlsData {
                guard let data = Data(base64Encoded: url) else {
                    continue
                }
                
                do {
                    var isStale = false
                    urls.append((try URL(resolvingBookmarkData: data, bookmarkDataIsStale: &isStale)))
                } catch {
                    continue
                }
            }
            
            DispatchQueue.global().async {
                self.accessibleFoldersShared = urls
            }
            
            return urls
        }
    }
    #endif
    
    /// The site-packages folder shared between app extensions.
    static var sitePackages: URL? {
        get {
            guard let data = UserDefaults.shared?.data(forKey: "sitePackagesFolder") else {
                return nil
            }
            
            do {
                var isStale = false
                let url = try URL(resolvingBookmarkData: data, bookmarkDataIsStale: &isStale)
                _ = url.startAccessingSecurityScopedResource()
                return url
            } catch {
                print(error.localizedDescription)
                return nil
            }
        }
        
        set {
            do {
                UserDefaults.shared?.set(try newValue?.bookmarkData(), forKey: "sitePackagesFolder")
            } catch {
                print(error.localizedDescription)
            }
        }
    }
    
    /// Folders readable and writable by Pyto.
    static var accessibleFoldersShared: [URL] {
        set {
            var strings = [String]()
            
            for url in newValue {
                do {
                    strings.append((try url.bookmarkData()).base64EncodedString())
                } catch {
                    continue
                }
            }
            
            UserDefaults.shared?.set(strings, forKey: "folders")
        }
        
        get {
            guard let urlsData = UserDefaults.shared?.stringArray(forKey: "folders") else {
                return []
            }
            
            var urls = [URL]()
            
            for url in urlsData {
                guard let data = Data(base64Encoded: url) else {
                    continue
                }
                
                do {
                    var isStale = false
                    urls.append((try URL(resolvingBookmarkData: data, bookmarkDataIsStale: &isStale)))
                } catch {
                    continue
                }
            }
            
            return urls
        }
    }
    
    #if MAIN
    /// Adds a folder to `accessibleFolders`.
    @IBAction func addFolder(_ sender: Any) {
        let picker = UIDocumentPickerViewController(documentTypes: ["public.folder"], in: .open)
        picker.delegate = self
        picker.allowsMultipleSelection = true
        present(picker, animated: true, completion: nil)
    }
    
    // MARK: - Table view controller
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        navigationItem.rightBarButtonItems?.append(editButtonItem)
        navigationItem.largeTitleDisplayMode = .never
        
        clearsSelectionOnViewWillAppear = true
    }
    
    override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return FoldersBrowserViewController.accessibleFolders.count
    }
    
    override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = UITableViewCell(style: .subtitle, reuseIdentifier: nil)
        
        cell.textLabel?.text = FileManager.default.displayName(atPath: FoldersBrowserViewController.accessibleFolders[indexPath.row].path)
        
        return cell
    }
    
    override func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        tableView.deselectRow(at: indexPath, animated: true)
    }
    
    override func tableView(_ tableView: UITableView, commit editingStyle: UITableViewCell.EditingStyle, forRowAt indexPath: IndexPath) {
        if editingStyle == .delete {
            FoldersBrowserViewController.accessibleFolders.remove(at: indexPath.row)
            tableView.deleteRows(at: [indexPath], with: .automatic)
        }
    }
    
    override func tableView(_ tableView: UITableView, canEditRowAt indexPath: IndexPath) -> Bool {
        return true
    }
    
    // MARK: - Document picker delegate
    
    func documentPicker(_ controller: UIDocumentPickerViewController, didPickDocumentsAt urls: [URL]) {
        for url in urls {
            if !FoldersBrowserViewController.accessibleFolders.contains(url.resolvingSymlinksInPath()) {
                _ = url.startAccessingSecurityScopedResource()
                FoldersBrowserViewController.accessibleFolders.append(url.resolvingSymlinksInPath())
            }
        }
        
        tableView.reloadData()
    }
    #endif
}
