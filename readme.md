# コーパスレコーダー

<p align="center">
  <img src="https://github.com/Mega-Gorilla/Voice_corpus_Recorder/blob/main/images/image1.png"/>
</p>

## 概要

このソフトウェアは、音声コーパスの作成を容易にするために設計された音声録音ヘルパーです。
ファイル名の管理や録音スクリプトの表示を自動化することで、コーパス録音のプロセス効率化を実現します。

音声コーパスの表示と録音機能、ファイル管理機能を備え、今までのコーパス作成で大変だったコーパス原稿の確認、ファイル名管理、再録音の作業を効率化します。

## 特徴

- **Corpus Display:** アプリケーションがサポートする音声コーパスを簡単に閲覧できます。
- **Recording Functionality:** ガイド付きプロンプトで声を録音し、コーパス作成時の一貫性と品質を保証します。
- **Automated Management:** コーパスファイル名と録音スクリプトの管理を自動で行い、手作業と潜在的なエラーを減らします。

## 対応コーパス
- **ita-corpus** - ITAコーパスは、合計424文からなる，音素バランスを考慮したパブリックドメインの日本語テキストコーパスです． https://github.com/Haruqa/ita-corpus
- **JVNV**  - JVNVは，言語音声と非言語音声から成る日本語感情音声コーパスです． https://sites.google.com/site/shinnosuketakamichi/research-topics/jvnv_corpus

※コーパスの追加依頼がございましたらissueより提案ください。

## インストール

Voice Recording Helperをインストールするには、システムにPythonがインストールされている必要があります。
以下の手順で始めましょう：

1. リポジトリをクローンするか、ソースコードをダウンロードしてください。
2. ソースコードがあるディレクトリで端末またはコマンドプロンプトを開きます。
3. 必要な依存関係をインストールするために、次のコマンドを実行してください：

```bash
pip install -r requirements.txt
```

## 使い方

必要な依存関係をインストールした後、Streamlitを使用してアプリケーションを開始できます。

起動するには、端末またはコマンドプロンプトで次のコマンドを実行するか、`run.bat` を実行してアプリケーションを開始できます。

```bash
streamlit run app.py
```

これにより、ウェブブラウザでアプリケーションが開始されます。画面上の指示に従って、音声コーパスを閲覧および録音してください。

録音された音声データは、同一ディレクトリ内のsaveフォルダーにwavファイルが保存されます。

## より詳しく

### Q:任意のコーパスを追加したい

A: コーパスレコーダーでは、/modules/corpus_dict.pyを編集することによって簡単に、任意のコーパスを追加することができます。詳細は、corpus_dict.pyを参照ください。

### Q:対応してほしいコーパスがあり、追加をお願いしたい。

A:コーパスの追加依頼は、Github issueよりご依頼ください。

## 貢献

対応ボイスコーパスの追加依頼、バグの報告がありましたら、Issuue機能より相談ください。

## ライセンス

このソフトウェアはMITライセンスの下でリリースされています。詳細については、ソースリポジトリのLICENSEファイルを参照してください。

<br/>


<br/>

# Voice Corpus Recorder

## Overview

This software is a Voice Recording Helper designed to facilitate the creation of voice corpora. It streamlines the process of corpus recording by automating file name management and the display of recording scripts. With features to display and record voice corpora, this tool simplifies the previously complex tasks involved in corpus recording, making it more efficient and user-friendly.

## Features

- **Corpus Display:** Easily view the voice corpora that are supported by the application.
- **Recording Functionality:** Record your voice with guided prompts, ensuring consistency and quality in corpus creation.
- **Automated Management:** Automatically handles the management of corpus file names and recording scripts, reducing manual effort and potential errors.

## Installation

To install the Voice Recording Helper, you need to have Python installed on your system. Follow these steps to get started:

1. Clone the repository or download the source code to your local machine.
2. Open a terminal or command prompt in the directory where you have the source code.
3. Run the following command to install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

After installing the necessary dependencies, you can start the application using Streamlit. To do so, run the following command in the terminal or command prompt:

```bash
streamlit run app.py
```

This will start the application in your default web browser. Follow the on-screen instructions to view and record voice corpora.

## Contributing

We welcome contributions from the community. Whether it's improving the documentation, fixing bugs, or adding new features, your contributions are appreciated. Please feel free to fork the repository and submit pull requests.

## License

This software is released under the MIT License. See the LICENSE file in the source repository for more information.