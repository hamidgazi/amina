; ==============================================================================
; Hamid's Master Hinglish Autocorrect Script for Windows
; Works seamlessly across WhatsApp Web, Instagram, Telegram, Chrome, Edge, etc.
; ==============================================================================
; To run: Install AutoHotkey (from autohotkey.com) and double-click this file.
; Pressing Ctrl + Esc at any time exits the script.
; ==============================================================================

#NoEnv
#SingleInstance force
SendMode Input
SetWorkingDir %A_ScriptDir%

TrayTip, Hinglish Autocorrect Active, Hamid's Hinglish Autocorrect is running in the background!, 3

; --- Top Pronouns & Addressing ---
::muje::mujhe
::tuje::tujhe
::mene::maine
::dusre::doosre
::tune::toone

; --- Common Verbs & Future Tense ---
::hu::hoon
::lunga::loonga
::karu::karoon
::dunga::doonga
::samaj::samajh
::jaunga::jaoonga
::batana::bataana
::samja::samjha

; --- Adverbs, Questions & Conjunctions ---
::zayada::zyada
::badme::baad mein
::kyu::kyun
::kese::kaise
::vese::waise

; --- General Quantifiers & Vocabulary ---
::kuch::kuchh
::eak::ek
::baate::baatein
::shadi::shaadi
::acha::achha

; --- Safety Whitelist (prevents miscorrection) ---
::thoda::thoda

; Exit shortcut: Ctrl + Esc closes the script
^Esc::ExitApp
