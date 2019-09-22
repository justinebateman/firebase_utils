# Firebase Utils - Python

Python Utility library for the [Google Firebase Admin SDK](https://firebase.google.com/docs/admin/setup)

## Installation

First install and setup the Admin SDK

```
pip install firebase-admin
```

Follow [these](https://firebase.google.com/docs/admin/setup) instructions to set up the GOOGLE_APPLICATION_CREDENTIALS environment variable 

Install these dependencies

```
pip install multipledispatch
```

To install firebase_utils as a module for usage anywhere on your machine:
- Clone this repo
- Open the folder in a terminal
- Enter the following cmd

```
pip install -e .
```

## Usage

When using any of these util functions in your python scripts ensure you initialise the SDK first with:

```
from firebase_utils import firebase_initialise

firebase_initialise.initialise_admin()
```

## Firebase push notifications

Example usage

```
from firebase_utils import firebase_initialise, firebase_message

firebase_initialise.initialise_admin()

firebase_message.send("Notification title", "Notification body")
```