"""
UIKit classes

This module contains all UIKit classes. You should not use this module to present an UI, there is the ``pyto_ui`` module for that. However, you can safely use classes like ``UIDevice``, ``UIImage``, ``UIFont`` etc.
"""

try:
    from rubicon.objc import ObjCClass
except ValueError:

    def ObjCClass(class_name):
        return None


def __class__(name):
    try:
        return ObjCClass(name)
    except NameError:
        return None


UIApplication = __class__("UIApplication")
UIDevice = __class__("UIDevice")
UITraitCollection = __class__("UITraitCollection")
UIDocument = __class__("UIDocument")
UIManagedDocument = __class__("UIManagedDocument")
UIPasteboard = __class__("UIPasteboard")
UIPasteConfiguration = __class__("UIPasteConfiguration")
NSUserActivity = __class__("NSUserActivity")
UIActivity = __class__("UIActivity")
UIActivityViewController = __class__("UIActivityViewController")
UIActivityItemProvider = __class__("UIActivityItemProvider")
UIStoryboard = __class__("UIStoryboard")
UIStoryboardSegue = __class__("UIStoryboardSegue")
UIStoryboardUnwindSegueSource = __class__("UIStoryboardUnwindSegueSource")
UIImageAsset = __class__("UIImageAsset")
NSDataAsset = __class__("NSDataAsset")
UINib = __class__("UINib")
NSExtensionContext = __class__("NSExtensionContext")
UIDocumentPickerExtensionViewController = __class__(
    "UIDocumentPickerExtensionViewController"
)
NSFileProviderExtension = __class__("NSFileProviderExtension")
UIInputViewController = __class__("UIInputViewController")
UILexicon = __class__("UILexicon")
UILexiconEntry = __class__("UILexiconEntry")
UIView = __class__("UIView")
UIStackView = __class__("UIStackView")
UIScrollView = __class__("UIScrollView")
UIActivityIndicatorView = __class__("UIActivityIndicatorView")
UIImageView = __class__("UIImageView")
UIPickerView = __class__("UIPickerView")
UIProgressView = __class__("UIProgressView")
UIControl = __class__("UIControl")
UIButton = __class__("UIButton")
UIDatePicker = __class__("UIDatePicker")
UIPageControl = __class__("UIPageControl")
UISegmentedControl = __class__("UISegmentedControl")
UISlider = __class__("UISlider")
UIStepper = __class__("UIStepper")
UISwitch = __class__("UISwitch")
UILabel = __class__("UILabel")
UITextField = __class__("UITextField")
UITextView = __class__("UITextView")
UIVisualEffect = __class__("UIVisualEffect")
UIVisualEffectView = __class__("UIVisualEffectView")
UIVibrancyEffect = __class__("UIVibrancyEffect")
UIBlurEffect = __class__("UIBlurEffect")
UIBarItem = __class__("UIBarItem")
UIBarButtonItem = __class__("UIBarButtonItem")
UIBarButtonItemGroup = __class__("UIBarButtonItemGroup")
UINavigationBar = __class__("UINavigationBar")
UISearchBar = __class__("UISearchBar")
UIToolbar = __class__("UIToolbar")
UITabBar = __class__("UITabBar")
UITabBarItem = __class__("UITabBarItem")
UIViewController = __class__("UIViewController")
UITableViewController = __class__("UITableViewController")
UICollectionViewController = __class__("UICollectionViewController")
UISplitViewController = __class__("UISplitViewController")
UINavigationController = __class__("UINavigationController")
UINavigationItem = __class__("UINavigationItem")
UIPageViewController = __class__("UIPageViewController")
UITabBarController = __class__("UITabBarController")
UISearchContainerViewController = __class__("UISearchContainerViewController")
UISearchController = __class__("UISearchController")
UIImagePickerController = __class__("UIImagePickerController")
UIVideoEditorController = __class__("UIVideoEditorController")
UIDocumentBrowserViewController = __class__("UIDocumentBrowserViewController")
UIDocumentPickerViewController = __class__("UIDocumentPickerViewController")
UIDocumentInteractionController = __class__("UIDocumentInteractionController")
UICloudSharingController = __class__("UICloudSharingController")
UIReferenceLibraryViewController = __class__("UIReferenceLibraryViewController")
UIPrinterPickerController = __class__("UIPrinterPickerController")
UIPresentationController = __class__("UIPresentationController")
NSLayoutConstraint = __class__("NSLayoutConstraint")
UILayoutGuide = __class__("UILayoutGuide")
NSLayoutDimension = __class__("NSLayoutDimension")
NSLayoutAnchor = __class__("NSLayoutAnchor")
NSLayoutXAxisAnchor = __class__("NSLayoutXAxisAnchor")
NSLayoutYAxisAnchor = __class__("NSLayoutYAxisAnchor")
UIFeedbackGenerator = __class__("UIFeedbackGenerator")
UIImpactFeedbackGenerator = __class__("UIImpactFeedbackGenerator")
UINotificationFeedbackGenerator = __class__("UINotificationFeedbackGenerator")
UISelectionFeedbackGenerator = __class__("UISelectionFeedbackGenerator")
UIWindow = __class__("UIWindow")
UIPopoverPresentationController = __class__("UIPopoverPresentationController")
UIPopoverBackgroundView = __class__("UIPopoverBackgroundView")
UIAlertController = __class__("UIAlertController")
UIAlertAction = __class__("UIAlertAction")
UIScreen = __class__("UIScreen")
UIScreenMode = __class__("UIScreenMode")
UIResponder = __class__("UIResponder")
UIEvent = __class__("UIEvent")
UITouch = __class__("UITouch")
UIPress = __class__("UIPress")
UIPressesEvent = __class__("UIPressesEvent")
UILongPressGestureRecognizer = __class__("UILongPressGestureRecognizer")
UIPanGestureRecognizer = __class__("UIPanGestureRecognizer")
UIGestureRecognizer = __class__("UIGestureRecognizer")
UIPinchGestureRecognizer = __class__("UIPinchGestureRecognizer")
UIScreenEdgePanGestureRecognizer = __class__("UIScreenEdgePanGestureRecognizer")
UISwipeGestureRecognizer = __class__("UISwipeGestureRecognizer")
UIRotationGestureRecognizer = __class__("UIRotationGestureRecognizer")
UITapGestureRecognizer = __class__("UITapGestureRecognizer")
UIDragInteraction = __class__("UIDragInteraction")
UIDropInteraction = __class__("UIDropInteraction")
UISpringLoadedInteraction = __class__("UISpringLoadedInteraction")
UIDragItem = __class__("UIDragItem")
UIDropProposal = __class__("UIDropProposal")
NSItemProvider = __class__("NSItemProvider")
UIDragPreviewParameters = __class__("UIDragPreviewParameters")
UIDragPreview = __class__("UIDragPreview")
UIDragPreviewTarget = __class__("UIDragPreviewTarget")
UITargetedDragPreview = __class__("UITargetedDragPreview")
UIPencilInteraction = __class__("UIPencilInteraction")
UIFocusSystem = __class__("UIFocusSystem")
UIFocusUpdateContext = __class__("UIFocusUpdateContext")
UIFocusMovementHint = __class__("UIFocusMovementHint")
UIFocusGuide = __class__("UIFocusGuide")
UIFocusDebugger = __class__("UIFocusDebugger")
UIFocusAnimationCoordinator = __class__("UIFocusAnimationCoordinator")
UIPreviewAction = __class__("UIPreviewAction")
UIPreviewActionGroup = __class__("UIPreviewActionGroup")
UIPreviewInteraction = __class__("UIPreviewInteraction")
UIApplicationShortcutIcon = __class__("UIApplicationShortcutIcon")
UIApplicationShortcutItem = __class__("UIApplicationShortcutItem")
UIMutableApplicationShortcutItem = __class__("UIMutableApplicationShortcutItem")
UIKeyCommand = __class__("UIKeyCommand")
UIMenuController = __class__("UIMenuController")
UIMenuItem = __class__("UIMenuItem")
UIInputView = __class__("UIInputView")
UIAccessibilityCustomAction = __class__("UIAccessibilityCustomAction")
UIAccessibilityElement = __class__("UIAccessibilityElement")
UIAccessibilityCustomRotor = __class__("UIAccessibilityCustomRotor")
UIAccessibilityCustomRotorItemResult = __class__("UIAccessibilityCustomRotorItemResult")
UIAccessibilityCustomRotorSearchPredicate = __class__(
    "UIAccessibilityCustomRotorSearchPredicate"
)
UIAccessibilityLocationDescriptor = __class__("UIAccessibilityLocationDescriptor")
UIImage = __class__("UIImage")
UIGraphicsRenderer = __class__("UIGraphicsRenderer")
UIGraphicsRendererContext = __class__("UIGraphicsRendererContext")
UIGraphicsRendererFormat = __class__("UIGraphicsRendererFormat")
UIGraphicsImageRenderer = __class__("UIGraphicsImageRenderer")
UIGraphicsImageRendererContext = __class__("UIGraphicsImageRendererContext")
UIGraphicsImageRendererFormat = __class__("UIGraphicsImageRendererFormat")
UIGraphicsPDFRenderer = __class__("UIGraphicsPDFRenderer")
UIGraphicsPDFRendererContext = __class__("UIGraphicsPDFRendererContext")
UIGraphicsPDFRendererFormat = __class__("UIGraphicsPDFRendererFormat")
UIColor = __class__("UIColor")
UIBezierPath = __class__("UIBezierPath")
NSShadow = __class__("NSShadow")
UIPrintInteractionController = __class__("UIPrintInteractionController")
UIPrintPageRenderer = __class__("UIPrintPageRenderer")
UIPrinter = __class__("UIPrinter")
UIPrintInfo = __class__("UIPrintInfo")
UIPrintPaper = __class__("UIPrintPaper")
UIPrintFormatter = __class__("UIPrintFormatter")
UIViewPrintFormatter = __class__("UIViewPrintFormatter")
UISimpleTextPrintFormatter = __class__("UISimpleTextPrintFormatter")
UIMarkupTextPrintFormatter = __class__("UIMarkupTextPrintFormatter")
NSLayoutManager = __class__("NSLayoutManager")
NSTextStorage = __class__("NSTextStorage")
UIFont = __class__("UIFont")
UIFontDescriptor = __class__("UIFontDescriptor")
UIFontMetrics = __class__("UIFontMetrics")
UITextChecker = __class__("UITextChecker")
NSTextContainer = __class__("NSTextContainer")
NSAttributedString = __class__("NSAttributedString")
UITextPosition = __class__("UITextPosition")
UITextRange = __class__("UITextRange")
UITextSelectionRect = __class__("UITextSelectionRect")
NSParagraphStyle = __class__("NSParagraphStyle")
NSMutableParagraphStyle = __class__("NSMutableParagraphStyle")
NSTextTab = __class__("NSTextTab")
NSTextAttachment = __class__("NSTextAttachment")
UITextInputTraits = __class__("UITextInputTraits")
UITextInputAssistantItem = __class__("UITextInputAssistantItem")
UITextInputMode = __class__("UITextInputMode")
UITextInputStringTokenizer = __class__("UITextInputStringTokenizer")
UIDictationPhrase = __class__("UIDictationPhrase")
UIWindowScene = __class__("UIWindowScene")
UIScene = __class__("UIScene")
UISceneSession = __class__("UISceneSession")
UISceneConfiguration = __class__("UISceneConfiguration")
UISceneActivationConditions = __class__("UISceneActivationConditions")
UIStatusBarManager = __class__("UIStatusBarManager")
UILargeContentViewerInteraction = __class__("UILargeContentViewerInteraction")
UIFontPickerViewController = __class__("UIFontPickerViewController")
UIFontPickerViewControllerConfiguration = __class__(
    "UIFontPickerViewControllerConfiguration"
)
UINavigationBarAppearance = __class__("UINavigationBarAppearance")
UIToolbarAppearance = __class__("UIToolbarAppearance")
UITabBarAppearance = __class__("UITabBarAppearance")
UITabBarItemAppearance = __class__("UITabBarItemAppearance")
UITabBarItemStateAppearance = __class__("UITabBarItemStateAppearance")
UIBarAppearance = __class__("UIBarAppearance")
UIBarButtonItemAppearance = __class__("UIBarButtonItemAppearance")
UIBarButtonItemStateAppearance = __class__("UIBarButtonItemStateAppearance")
UIHoverGestureRecognizer = __class__("UIHoverGestureRecognizer")
UIMenu = __class__("UIMenu")
UIMenuElement = __class__("UIMenuElement")
UIContextMenuInteraction = __class__("UIContextMenuInteraction")
UITargetedPreview = __class__("UITargetedPreview")
UIPreviewTarget = __class__("UIPreviewTarget")
UIPreviewParameters = __class__("UIPreviewParameters")
UIAction = __class__("UIAction")
UICommand = __class__("UICommand")
UIMutableKeyCommand = __class__("UIMutableKeyCommand")
UIScreenshotService = __class__("UIScreenshotService")
UISearchTextField = __class__("UISearchTextField")
UISearchToken = __class__("UISearchToken")
UITextFormattingCoordinator = __class__("UITextFormattingCoordinator")
UITextInteraction = __class__("UITextInteraction")
UIMenuSystem = __class__("UIMenuSystem")

__all__ = [
    "UIApplication",
    "UIDevice",
    "UITraitCollection",
    "UIDocument",
    "UIManagedDocument",
    "UIPasteboard",
    "UIPasteConfiguration",
    "NSUserActivity",
    "UIActivity",
    "UIActivityViewController",
    "UIActivityItemProvider",
    "UIStoryboard",
    "UIStoryboardSegue",
    "UIStoryboardUnwindSegueSource",
    "UIImageAsset",
    "NSDataAsset",
    "UINib",
    "NSExtensionContext",
    "UIDocumentPickerExtensionViewController",
    "NSFileProviderExtension",
    "UIInputViewController",
    "UILexicon",
    "UILexiconEntry",
    "UIView",
    "UIStackView",
    "UIScrollView",
    "UIActivityIndicatorView",
    "UIImageView",
    "UIPickerView",
    "UIProgressView",
    "UIControl",
    "UIButton",
    "UIDatePicker",
    "UIPageControl",
    "UISegmentedControl",
    "UISlider",
    "UIStepper",
    "UISwitch",
    "UILabel",
    "UITextField",
    "UITextView",
    "UIVisualEffect",
    "UIVisualEffectView",
    "UIVibrancyEffect",
    "UIBlurEffect",
    "UIBarItem",
    "UIBarButtonItem",
    "UIBarButtonItemGroup",
    "UINavigationBar",
    "UISearchBar",
    "UIToolbar",
    "UITabBar",
    "UITabBarItem",
    "UIViewController",
    "UITableViewController",
    "UICollectionViewController",
    "UISplitViewController",
    "UINavigationController",
    "UINavigationItem",
    "UIPageViewController",
    "UITabBarController",
    "UISearchContainerViewController",
    "UISearchController",
    "UIImagePickerController",
    "UIVideoEditorController",
    "UIDocumentBrowserViewController",
    "UIDocumentPickerViewController",
    "UIDocumentInteractionController",
    "UICloudSharingController",
    "UIReferenceLibraryViewController",
    "UIPrinterPickerController",
    "UIPresentationController",
    "NSLayoutConstraint",
    "UILayoutGuide",
    "NSLayoutDimension",
    "NSLayoutAnchor",
    "NSLayoutXAxisAnchor",
    "NSLayoutYAxisAnchor",
    "UIFeedbackGenerator",
    "UIImpactFeedbackGenerator",
    "UINotificationFeedbackGenerator",
    "UISelectionFeedbackGenerator",
    "UIWindow",
    "UIPopoverPresentationController",
    "UIPopoverBackgroundView",
    "UIAlertController",
    "UIAlertAction",
    "UIScreen",
    "UIScreenMode",
    "UIResponder",
    "UIEvent",
    "UITouch",
    "UIPress",
    "UIPressesEvent",
    "UILongPressGestureRecognizer",
    "UIPanGestureRecognizer",
    "UIGestureRecognizer",
    "UIPinchGestureRecognizer",
    "UIScreenEdgePanGestureRecognizer",
    "UISwipeGestureRecognizer",
    "UIRotationGestureRecognizer",
    "UITapGestureRecognizer",
    "UIDragInteraction",
    "UIDropInteraction",
    "UISpringLoadedInteraction",
    "UIDragItem",
    "UIDropProposal",
    "NSItemProvider",
    "UIDragPreviewParameters",
    "UIDragPreview",
    "UIDragPreviewTarget",
    "UITargetedDragPreview",
    "UIPencilInteraction",
    "UIFocusSystem",
    "UIFocusUpdateContext",
    "UIFocusMovementHint",
    "UIFocusGuide",
    "UIFocusDebugger",
    "UIFocusAnimationCoordinator",
    "UIPreviewAction",
    "UIPreviewActionGroup",
    "UIPreviewInteraction",
    "UIApplicationShortcutIcon",
    "UIApplicationShortcutItem",
    "UIMutableApplicationShortcutItem",
    "UIKeyCommand",
    "UIMenuController",
    "UIMenuItem",
    "UIInputView",
    "UIAccessibilityCustomAction",
    "UIAccessibilityElement",
    "UIAccessibilityCustomRotor",
    "UIAccessibilityCustomRotorItemResult",
    "UIAccessibilityCustomRotorSearchPredicate",
    "UIAccessibilityLocationDescriptor",
    "UIImage",
    "UIGraphicsRenderer",
    "UIGraphicsRendererContext",
    "UIGraphicsRendererFormat",
    "UIGraphicsImageRenderer",
    "UIGraphicsImageRendererContext",
    "UIGraphicsImageRendererFormat",
    "UIGraphicsPDFRenderer",
    "UIGraphicsPDFRendererContext",
    "UIGraphicsPDFRendererFormat",
    "UIColor",
    "UIBezierPath",
    "NSShadow",
    "UIPrintInteractionController",
    "UIPrintPageRenderer",
    "UIPrinter",
    "UIPrintInfo",
    "UIPrintPaper",
    "UIPrintFormatter",
    "UIViewPrintFormatter",
    "UISimpleTextPrintFormatter",
    "UIMarkupTextPrintFormatter",
    "NSLayoutManager",
    "NSTextStorage",
    "UIFont",
    "UIFontDescriptor",
    "UIFontMetrics",
    "UITextChecker",
    "NSTextContainer",
    "NSAttributedString",
    "UITextPosition",
    "UITextRange",
    "UITextSelectionRect",
    "NSParagraphStyle",
    "NSMutableParagraphStyle",
    "NSTextTab",
    "NSTextAttachment",
    "UITextInputTraits",
    "UITextInputAssistantItem",
    "UITextInputMode",
    "UITextInputStringTokenizer",
    "UIDictationPhrase",
    "UIWindowScene",
    "UIScene",
    "UISceneSession",
    "UISceneConfiguration",
    "UISceneActivationConditions",
    "UIStatusBarManager",
    "UILargeContentViewerInteraction",
    "UIFontPickerViewController",
    "UIFontPickerViewControllerConfiguration",
    "UINavigationBarAppearance",
    "UIToolbarAppearance",
    "UITabBarAppearance",
    "UITabBarItemAppearance",
    "UITabBarItemStateAppearance",
    "UIBarAppearance",
    "UIBarButtonItemAppearance",
    "UIBarButtonItemStateAppearance",
    "UIHoverGestureRecognizer",
    "UIMenu",
    "UIMenuElement",
    "UIContextMenuInteraction",
    "UITargetedPreview",
    "UIPreviewTarget",
    "UIPreviewParameters",
    "UIAction",
    "UICommand",
    "UIMutableKeyCommand",
    "UIScreenshotService",
    "UISearchTextField",
    "UISearchToken",
    "UITextFormattingCoordinator",
    "UITextInteraction",
    "UIMenuSystem",
]
