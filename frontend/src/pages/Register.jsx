import Container from "../components/shared/Container"
import AuthCard from "../components/shared/AuthCard"
import AuthButton from "../components/shared/AuthButton"
import SiteDescription from "../components/shared/SiteDescription"
import { Helmet } from "react-helmet"

const Register = () => {
    return (
        <>
            <Helmet>
                <title>Sign up for Network</title>
            </Helmet>
            <Container additionalClasses="flex justify-between">
                <SiteDescription />
                <AuthCard>
                    <form className="flex flex-col items-center justify-center space-y-4 mb-2">
                        <input className="w-full py-2 focus:outline-none rounded-md border border-stone-200 px-2 focus:ring-2" type="text" placeholder="Fullname" />
                        <input className="w-full py-2 focus:outline-none rounded-md border border-stone-200 px-2 focus:ring-2" type="email" placeholder="Email" />
                        <input className="w-full py-2 focus:outline-none rounded-md border border-stone-200 px-2 focus:ring-2" type="text" placeholder="Username" />
                        <input className="w-full py-2 focus:outline-none rounded-md border border-stone-200 px-2 focus:ring-2" type="password" placeholder="Password" />
                        <input className="w-full py-2 focus:outline-none rounded-md border border-stone-200 px-2 focus:ring-2" type="password" placeholder="Confirm Password" />
                        <AuthButton>Sign up</AuthButton>
                    </form>
                    <p className="text-sm text-slate-500">Already have an account?</p>
                    <a className="inline-block text-sm text-indigo-400 hover:text-indigo-500 hover:underline hover:decoration-indigo-500" href="#">Log in</a>
                </AuthCard>
            </Container>
        </>

    )
}

export default Register