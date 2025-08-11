languages = {
    "en",  # English language
    "ar",  # Arabic language
}

messages = {
    "authentication": {
        # class
        "SignIn": {
            # fun
            "check_password": {
                "incorrect": {
                    "en": "The password is incorrect",
                    "ar": "كلمة المرور غير صحيحة"
                }
            },
        },
        "SignUp": {
            "login_success": {
                "en": "You are logged in successfully",
                "ar": "لقد قمت بتسجيل الدخول بنجاح"
            },
            "check_name": {
                "none": {
                    "en": "Please enter your name",
                    "ar": "من فضلك أدخل إسمك"
                },
                "min": {
                    "en": "Your name is too small, it should be more than two letters",
                    "ar": "اسمك صغير جدًا ، يجب أن يكون أكثر من حرفين"
                },
                "max": {
                    "en": "Your name is too big, it should be less than 30 characters",
                    "ar": "اسمك كبير جدًا ، يجب أن يكون اقل من 30 حرف"
                }
            },
            "check_email": {
                "none": {
                    "en": "Please enter your email",
                    "ar": "من فضلك أدخل بريدك الإلكتروني"

                },
                "max": {
                    "en": "Your email is too big, it should be less than 50 characters",
                    "ar": "بريدك الإلكتروني كبير جدًا ، يجب أن يكون اقل من ٥٠ حرف"
                },
                "already_exists": {
                    "en": "You cannot use this email because it is linked to a different account.",
                    "ar": "لا يمكنك استخدام هذا البريد لأنه مرتبط بحساب مختلف"
                },
                "incorrect": {
                    "en": "This email is incorrect",
                    "ar": "هذا البريد الإلكتروني غير صحيح"
                }

            },
            "check_password": {
                "none": {
                    "en": "Please enter the password",
                    "ar": "من فضلك ادخل كلمة السر"
                },
                "min": {
                    "en": "The password is very small, it must be more than 8 letters or numbers",
                    "ar": "كلمة المرور صغيرة جدًا ، يجب أن تكون أكثر من 8 أحرف أو أرقام"
                },
                "max": {
                    "en": "The password is too large, it must be less than 50 characters or numbers",
                    "ar": "كلمة المرور كبيرة جدًا ، يجب أن تكون اقل من ٥٠  حرف أو رقام"
                },
                "lowercase": {
                    "en": "Password must contain at least one lowercase letter.",
                    "ar": "كلمة المرور يجب أن تحتوي على حرف صغير واحد على الأقل"
                },
                "capital": {
                    "en": "Password must contain at least one capital letter.",
                    "ar": "كلمة المرور يجب أن تحتوي على حرف كبير واحد على الأقل"
                },
                "number": {
                    "en": "Password must contain at least one number",
                    "ar": "كلمة المرور يجب أن تحتوي على رقم واحد على الأقل"
                },
                "special": {
                    "en": "The password must contain at least one special character.",
                    "ar": "كلمة المرور يجب أن تحتوي على رمز خاص واحد على الأقل"
                },

                "name_in": {
                    "en": "To protect your account, please do not enter your name in the password",
                    "ar": "لحماية حسابك ، يرجى عدم إدخال اسمك في كلمة المرور"
                },
                "email_in": {
                    "en": "To protect your account, please do not enter your email in the password",
                    "ar": "لحماية حسابك ، يرجى عدم إدخال بريدك الإلكتروني في كلمة المرور"
                },
                "arabic": {
                    "ar": "كلمة المرور لا يجب أن تحتوي على أحرف عربية.",
                    "en": "Password must not contain Arabic letters."
                },
                "contains_formation": {
                    "ar": "كلمة المرور لا يجب أن تحتوي على تشكيل عربي.",
                    "en": "Password must not contain Arabic diacritics (tashkeel)."
                },
                "space": {
                    "ar": "لا تنس بالمسافات في كلمة المرور.",
                    "en": "Don't forget the spaces in your password."
                }
            },

        },
    },
    "Alert": {
        "not_found": {
            "en": "Alert not found",
            "ar": "لم يتم العثور على التنبيه",
        },
        "check_stock": {
            "none": {
                "en": "Stock symbol is required",
                "ar": "رمز السهم مطلوب",
            },
            "not_found": {
                "en": "Stock not found",
                "ar": "لم يتم العثور على السهم",
            },
        },
        "check_type": {
            "invalid": {
                "en": "Invalid alert type",
                "ar": "نوع التنبيه غير صحيح",
            },
        },
        "check_condition": {
            "invalid": {
                "en": "Invalid condition",
                "ar": "الشرط غير صحيح",
            },
        },
        "check_threshold": {
            "invalid": {
                "en": "Invalid threshold value",
                "ar": "قيمة الحد غير صحيحة",
            },
        },
        "check_duration": {
            "invalid": {
                "en": "Invalid duration value",
                "ar": "قيمة المدة غير صحيحة",
            },
        },
    },
}
