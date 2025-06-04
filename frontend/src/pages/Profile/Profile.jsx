import React from "react";
import styles from "./Profile.module.scss";
import Header from "../../components/Header/Header";
import Footer from "../../components/Footer/Footer";

const Profile = () => {
    const user = { email: "exemple@mail.com" };
    return (
        <div className={styles.profile}>
            <Header />
            <main>
                <h2>Mon profil</h2>
                <p>Email : {user.email}</p>
            </main>
            <Footer />
        </div>
    );
};
export default Profile;
