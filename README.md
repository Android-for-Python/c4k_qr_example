Camera4Kivy QR Example
======================

*Everything You Need to Read a Restaurant Menu.*

# Overview

Long press or double tap on a highlighed QR, this opens the url encoded in the QR code. Mouse users need to have the mouse pointer inside the highlighted QR.

Available on most of the [usual platforms](https://github.com/Android-for-Python/Camera4Kivy/#tested-examples-and-platforms).

On a desktop the example assumes a builtin camera facing the user, so the Preview is mirrored. If you want to point a freely mounted camera at a QR code you may want to set the [Camera4Kivy mirror option False]((https://github.com/Android-for-Python/Camera4Kivy/#mirror)). 

The example demonstrates basic usage of the image analysis api. Analyzing image frames, and replacing the Preview contents with new image (including when mirrored).

# Install

This example depends on Camera4Kivy. **[Read about Camera4Kivy](https://github.com/Android-for-Python/Camera4Kivy#camera4kivy)** because, depending on the platform you may need to install a [camera provider](https://github.com/Android-for-Python/camera4kivy#camera-provider). In addition the example depends on pyzbar and pillow.

## Windows

`pip3 install pillow pyzbar camera4kivy`

## MacOS

`brew install zbar`

`pip3 install pillow pyzbar camera4kivy`

## Linux

`sudo apt-get install libzbar0`

`pip3 install pillow pyzbar camera4kivy`

## Android

Camera4Kivy depends on Buildozer 1.3.0 or later

`pip3 install buildozer`

`sudo apt-get install gettext`  some hosts already have this installed.

The example includes a [camera provider](https://github.com/Android-for-Python/camera4kivy#android-camera-provider) and a [buildozer.spec](https://github.com/Android-for-Python/camera4kivy#buildozerspec).


## iOS

**This example is not available on iOS due to these `kivy-ios` issues [676](https://github.com/kivy/kivy-ios/issues/676) and [681](https://github.com/kivy/kivy-ios/issues/681).** Use of the image analysis api, and of Python's Webbrowser have not been tested - expect the unexpected.

If/when these issues are addressed the install instructions will be similar to:

```
toolchain build libzbar
toolchain pip install pillow pyzbar camera4kivy
```

Permission to use the camera is **required** by iOS. To enable permission edit `<project>-ios/<project-Info.plist`, this file is created by Xcode. This entry must be added:

To enable use of the Camera add:
```
        <key>NSCameraUsageDescription</key>
	<string> </string>
```
