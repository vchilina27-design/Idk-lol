# Zip & IPA Packer

A simple Python script to pack files and directories into a .zip or .ipa archive.

## Usage

```bash
python3 zip_packer.py <source_path> <output_filename>
```

Example:
```bash
python3 zip_packer.py ./my_folder my_archive.zip
python3 zip_packer.py ./Payload my_app.ipa
```

## iOS IPA Support

### How to Create an IPA File

To create a valid `.ipa` file for iOS:
1. Create a folder named `Payload`.
2. Move your `.app` folder into the `Payload` folder.
3. Run the script:
   ```bash
   python3 zip_packer.py Payload my_app.ipa
   ```

### How to Sign and Install with Esign

Once you have generated your `.ipa` file, you can sign and install it on your iPhone using **Esign**:

1. **Import IPA**:
   - Send the `.ipa` file to your iPhone (via AirDrop, iCloud, or a web link).
   - Open **Esign** and tap on **File**.
   - Select the `.ipa` file you just uploaded.
2. **Sign IPA**:
   - Tap on the `.ipa` file in Esign.
   - Select **Signature**.
   - Choose your developer certificate or a free signing certificate.
   - Tap **Signature** again to confirm.
3. **Install**:
   - After signing is complete, a prompt will appear.
   - Tap **Install** to add the application to your Home Screen.
