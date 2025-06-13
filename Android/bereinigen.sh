#!/bin/bash
echo "🧹 Cleaning local buildozer project files..."
rm -rf ~/.gradle 
rm -rf ~/.buildozer/android/platform
rm -rf ~/.android

echo "✅ Clean complete. SDK and NDK preserved."

