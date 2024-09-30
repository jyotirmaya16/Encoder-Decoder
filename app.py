import streamlit as st
import string

#atbash_cipher incoder logic 
def atbash_cipher(x):
    import string
    a=string.ascii_lowercase
   
    p=x.lower() #--------------- logic start
    q=p.split()

    final_encode0=[]
    for n in q:
        encode=''   
        for i in n:
            firstdiff=abs(1 - (a.index(i)+1)) #=1 for cancellout the n-1 rule in indexing 
            finalencode= a[(26-firstdiff)-1] #-1 for cancellout the n-1 rule in indexing
            encode=encode+finalencode
        final_encode0.append(encode)
    final_encode1=" ".join(final_encode0)

    return(final_encode1)

#a1z26 encode_____________________________
def a1z26_encode(x):
    r=x.lower()
    r=r.split()

    import string
    a=string.ascii_lowercase
    b=[n for n in range(1,27)]
    d={}

    for n in range(26):
        d[a[n]]=b[n]


    final_encode0=[]
    for n in r:
        encode=""
        for i in n:
           t=d[i]
           encode=encode+str(t)+" "
        final_encode0.append(encode)
    final_encode1="".join(final_encode0)
    return(final_encode1)


#a1z26 decode_______________________________________
def a1z26_decode(x):
    r=x.lower()
    r=r.split()

    import string
    a=string.ascii_lowercase #-----------
    b=[str(n) for n in range(1,27)]
    d={}

    for n in range(26):
        d[b[n]]=a[n] #--------------

    final_encode0=[]
    encode=""
    for n in r:
        t=d[n]
        encode=encode+t
        final_encode0.append(encode)
    return(encode)

#main encode and decode __________________________
def a1z26(x):
    z=x
    z=z.split()
    
# Check if it's an encoding case (i.e., contains alphabetic characters)
    if z[0].isnumeric()==False:
        try:
          return(a1z26_encode(x))
        except:
            return("Note : There should not be any Numbers, punctuation, and special characters while encoding")
        
# Check if it's a decoding case (i.e., contains numeric values)     
    elif z[0].isnumeric() == True:
        for i in z:
            # If any number in the list is greater than 26, return an error message
            if int(i) > 26:
                return "Error: Numbers must be less than or equal to 26. Or you can put some space in between them "
        
        try:
            return a1z26_decode(x)
        except:
            return "Note: Only numeric values are allowed for decoding. Alphabets, punctuation, and special characters are not supported."
             

#streamlit app ________________

import streamlit as st

# Add custom CSS to style the image banner with overlayed text
st.markdown(
    """
    <style>
    .banner-container {
        position: relative;
        text-align: center;
        color: white;
    }
    .banner-image {
        width: 100%;  /* Set the width of the image to take up full space */
        height: auto;  /* Adjust the height of the image */
    }
    .banner-text {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        font-size: 36px;
        font-weight: bold;
        color: #00f03b;  /* Change this color to any color you want */
    }
    </style>
    """, unsafe_allow_html=True
)

# Select Cipher Choice
cipher_choice = st.selectbox("Choose your Encoder/Decoder:", ["A1Z26", "Atbash Cipher"])

# HTML block with image banner and overlayed text
if cipher_choice == "A1Z26":
    st.markdown(
        """
        <div class="banner-container">
            <img src="https://raw.githubusercontent.com/jyotirmaya16/Text-Encryption-Decryption-App/refs/heads/main/Screenshot%20(121).jpg" class="banner-image" alt="Banner Image">
            <div class="banner-text">A1Z26 Encoder/Decoder</div>
        </div>
        """, unsafe_allow_html=True
    )
else:
    st.markdown(
        """
        <div class="banner-container">
            <img src="https://raw.githubusercontent.com/jyotirmaya16/Text-Encryption-Decryption-App/refs/heads/main/Screenshot%20(121).jpg" class="banner-image" alt="Banner Image">
            <div class="banner-text">Atbash Cipher Encoder/Decoder</div>
        </div>
        """, unsafe_allow_html=True
    )

# User Input
user_input = st.text_input("Enter your message:")

if st.button('Process') or user_input:
    if user_input:
        # Call the appropriate function based on the user's choice
        if cipher_choice == "A1Z26":
            result = a1z26(user_input)  # Call A1Z26 function
        elif cipher_choice == "Atbash Cipher":
            try:
                result = atbash_cipher(user_input)  # Call Atbash Cipher function
            except:
                result = '''Note: Only alphabets are allowed. Numbers, punctuation, and special characters are not supported.
                        Try switching to A1Z26 
                       '''
        
        # Display the result
        st.write(result)
    else:
        st.write("Please enter some text/number.")


st.markdown(
    """
    <style>
    .small-button {
        display: inline-block;
        padding: 8px 16px;
        font-size: 14px;
        font-weight: bold;
        text-align: center;
        color: white;
        background-color: #d4e6f1; 
        border: none;
        border-radius: 4px;
        text-decoration: none;
        cursor: pointer;
        margin-top: 10px;
    }
    </style>
    """, unsafe_allow_html=True
)

# Add the button as a link
st.markdown(
    """
    <a href="https://github.com/jyotirmaya16/Text-Encryption-Decryption-App?tab=readme-ov-file#text-encryptiondecryption-app" target="_blank" class="small-button">Learn More</a>
    """, unsafe_allow_html=True
)


















       
# cipher_choice = st.selectbox("Choose your Encoder/Decoder:", ["A1Z26", "Atbash Cipher"])

# if cipher_choice == "A1Z26":
#     st.title("A1Z26 Encoder/Decoder")
# else:
#     st.title("Atbash Cipher Encoder/Decoder")

# user_input = st.text_input("Enter your messege:")

# if st.button('Process') or user_input:
#     if user_input:
#         # Call the appropriate function based on the user's choice
#         if cipher_choice == "A1Z26":
#             result = a1z26(user_input)  # Call A1Z26 function
#         elif cipher_choice == "Atbash Cipher":
#             try:
#               result = atbash_cipher(user_input)  # Call Atbash Cipher function
#             except:
#               result = '''Note: Only alphabates are allowed. number, punctuation, and special characters are not supported
#                         Try swithing to a1z26 
#                        '''
        
#         # Display the result
#         st.write(result)
#     else:
#         st.write("Please enter some text/number.")



         





