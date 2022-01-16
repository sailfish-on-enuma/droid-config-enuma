# These and other macros are documented in ../droid-configs-device/droid-configs.inc
# Feel free to cleanup this file by removing comments, once you have memorised them ;)

%define device enuma
%define vendor xiaomi

%define vendor_pretty Xiaomi
%define device_pretty Xiaomi Pad 5 Pro 5G

# Community HW adaptations need this
%define community_adaptation 1

# Sailfish OS is considered to-scale, if in the App Grid you get 4-in-a-row icons,
# and 2-in-a-row or 3-in-a-row app covers in the Home Screen, depending on
# how many apps are open.
# For 4-5.5" device screen sizes of 16:9 ratio, use this formula (hold portrait):
# pixel_ratio = 4.5/DiagonalDisplaySizeInches * HorizontalDisplayResolution/540
# Other screen sizes and ratios will require more trial-and-error.
%define pixel_ratio 1.0

%define have_modem 1
%define android_version_major 11

%include droid-configs-device/droid-configs.inc
%include patterns/patterns-sailfish-device-adaptation-enuma.inc
%include patterns/patterns-sailfish-device-configuration-enuma.inc

# IMPORTANT if you want to comment out any macros in your .spec, delete the %
# sign, otherwise they will remain defined! E.g.:
#define some_macro "I'll not be defined because I don't have % in front"
