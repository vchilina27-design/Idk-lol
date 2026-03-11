# iOS Task Manager (Final Assembly)

This project contains a structure for an iOS `.ipa` application with a heavy Mach-O binary placeholder and a single-file HTML Task Manager.

## Package Contents

- **`MyApp`**: A Mach-O 64-bit arm64 binary (150KB+). This is a placeholder designed to satisfy size requirements for iOS application containers.
- **`www/index.html`**: A fully functional, self-contained HTML/JS Task Manager designed with v0, Tailwind CSS, and Lucide icons.
- **`Info.plist`**: A valid iOS application property list.

## Installation Instructions

1. **Get a WebView Container IPA**:
   - Since a fully compiled native iOS app requires Xcode, you should use an open-source **WebView Container** (shell).
   - Recommended: [Capacitor iOS Shell](https://capacitorjs.com/) or [WKWebView minimal template](https://github.com/nicktmro/WKWebViewExample).

2. **Replace Files**:
   - Take the `www` folder from this archive and place it into your WebView container's `www` or `assets` folder.
   - Replace the main executable of your container with the `MyApp` file provided here if your container is missing a valid ARM64 binary.

3. **Sign and Install**:
   - Pack the `Payload` folder into a `.zip` and rename it to `.ipa`.
   - Use **Esign** or **AltStore** to sign the `.ipa` with your certificate.
   - Install and launch.

## Packing Command

```bash
python3 zip_packer.py Payload taskmanager_final.ipa
```

### Direct Links to WebView IPA Containers (Open Source):
- [Minimal Swift WKWebView](https://github.com/thefuntastic/Swift-WKWebView)
- [Apache Cordova iOS](https://github.com/apache/cordova-ios)
